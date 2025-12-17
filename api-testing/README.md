# 📘 API Testing – Reqres & Alternate API Suite

This module contains the API automation suite for the QA Automation Assignment.

It demonstrates:

✔ Functional API testing using pytest + requests

✔ Positive, negative, and smoke test design

✔ Graceful handling of Cloudflare 403 blocks

✔ A fallback alternate API test suite using JSONPlaceholder

✔ Load testing using Locust

✔ HTML reporting for CI/Manual execution

## 📋 Table of Contents

1. [Overview](#-overview)
2. [Project Structure](#-project-structure)
3. [Prerequisites](#-prerequisites)
4. [Installation](#-installation)
5. [Running Tests](#-running-tests)
6. [HTML Reports](#-html-reports)
7. [Design Choices](#-design-choices)
8. [Simple API Tests & Manual Test Cases (Fundamentals Layer)](#-simple-api-tests--manual-test-cases-fundamentals-layer)
9. [Load Testing](#-load-testing)
10. [Troubleshooting](#-troubleshooting)
11. [Contact](#-contact)
12. [Summary](#-summary)

## 🎯 Overview

This API test suite automates essential API workflows for testing.

### ✔ Current Test Coverage

- GET List Users
- GET Single User
- POST Create User
- POST Register User
- Negative Scenarios (Non-existing User, Missing Password, Invalid Endpoints)

All tests use **Pytest + Requests** for clean, maintainable automation.

**Average execution time:** 10–15 seconds

## 📁 Project Structure

```
api-testing/
│
├── tests/
│   ├── test_reqres_api.py      # Primary API tests (Reqres)
│   └── test_alt_api.py         # Alternate API tests (JSONPlaceholder)
│
├── locustfile.py               # Load test script
├── pytest.ini                  # Marker configuration
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

### Why Two Test Files?

Reqres is sometimes protected by Cloudflare and may block automated Python tests.

To ensure all functional logic still runs, an alternate test suite (`test_alt_api.py`) executes the same test scenarios against a stable API:

👉 https://jsonplaceholder.typicode.com

This guarantees:

- Tests always run successfully
- CI does not fail due to Cloudflare
- Reviewers can still evaluate your automation logic

## ✅ Prerequisites

Before running the API tests, ensure you have:

- **Python 3.7+**
- **Internet connection** (tests run against live APIs)

## 🔧 Installation

From the project root:

```bash
cd api-testing
pip install -r requirements.txt
```

### Key Dependencies

- pytest
- requests
- pytest-html
- locust (optional)

## 🚀 Running Tests

### Option 1: Run All API Tests (Verbose Output)

```bash
pytest -v
```

**Expected Behavior:**

| Test File | Expected Outcome |
|-----------|------------------|
| `test_alt_api.py` | ✅ Passes (JSONPlaceholder is stable) |
| `test_reqres_api.py` | ⚠️ May fail or skip because of Cloudflare blocking |

This is expected and documented.

### Option 2: Generate HTML Report

```bash
pytest -v --html=api-report.html --self-contained-html
```

This generates a standalone HTML report (`api-report.html`) containing:

- Execution summary
- Test duration
- Environment details
- Colored pass/fail results
- Detailed failure messages

### Option 3: Run Only Reqres Tests

```bash
pytest -v tests/test_reqres_api.py
```

### Option 4: Run Only Alternate API Tests

```bash
pytest -v tests/test_alt_api.py
```

This is useful when Reqres is blocked.

### Option 5: Marker-Based Execution

```bash
pytest -v -m api
pytest -v -m smoke
pytest -v -m positive
pytest -v -m negative
```

Defined in `pytest.ini`:

```ini
[pytest]
markers =
    api: API tests
    positive: Positive workflow tests
    negative: Error handling tests
    smoke: Quick validation tests
```

## 📊 HTML Reports

To open the generated HTML report:

```bash
# Windows
start api-report.html

# macOS
open api-report.html

# Linux
xdg-open api-report.html
```

HTML report includes:

- Test results
- Execution environment
- Traceback for failures
- Pass/Fail summary with timing

## 🎨 Design Choices

### 1. Pytest Framework

Organizes code with:

- **Test functions** → clear test scenarios
- **Markers** → categorize tests (smoke, positive, negative)
- **Fixtures** → reusable setup/teardown

This makes tests readable and easy to extend.

### 2. Cloudflare Handling

All Reqres tests include a helper:

```python
def skip_if_forbidden(response):
    if response.status_code == 403:
        pytest.skip("Cloudflare blocked the request.")
```

So your test run will show:

```
SKIPPED Cloudflare blocked the request.
```

instead of `FAILED`, avoiding misleading failures.

### 3. Alternate API Suite

When Reqres is blocked, the alternate suite (`test_alt_api.py`) ensures:

- Your functional test logic is still validated
- API scenarios still execute (GET, POST, negative tests)
- CI pipelines do not show failures caused by external websites

This suite mirrors:

| Reqres Test | JSONPlaceholder Equivalent |
|-------------|---------------------------|
| GET /users?page=2 | GET /users |
| GET /users/2 | GET /users/2 |
| POST /users | POST /posts |
| GET non-existing | GET user/99999 |
| POST /register (invalid) | POST /register → 404 |

All tests are stable and deterministic.

### 4. Test Coverage

Tests cover:

- **Positive scenarios** → GET list users, GET single user, POST create user, POST register user
- **Negative scenarios** → GET non-existing user, POST register missing password, Invalid endpoint
- **Assertions** → HTTP status codes, Required JSON keys, Field values, Error messages, Response structure

## 🧩 Simple API Tests & Manual Test Cases (Fundamentals Layer)

Alongside the PyTest-based API automation framework, this module also includes a simple API test script and manual test case documentation to demonstrate strong testing fundamentals.

### 📄 Files Included

- **`simple_api_test.py`** – A lightweight API testing script written using Python's `requests` library. It avoids frameworks and focuses on clear, step-by-step validation of API responses.
- **`testcase.md`** – Contains manual API test cases with objectives, endpoints, test steps, and expected results. These test cases serve as the foundation for both the simple script and the PyTest-based tests.

### 🎯 Purpose

This fundamentals layer is included to:

- Demonstrate manual API test design
- Show how test cases are translated into automation
- Provide easy-to-explain API tests for interviews
- Maintain clear traceability between test cases and code
- Ensure reliability when primary APIs are blocked or unavailable

### ▶️ Run the Simple API Tests

```bash
cd api-testing
python simple_api_test.py
```

💡 **The simple API script complements the PyTest framework tests and is intended to highlight core API testing concepts before introducing advanced automation patterns.**

## ⚡ Load Testing

A Locust script is included to measure response performance of API endpoints.

**Run in headless mode:**

```bash
locust -f locustfile.py --headless -u 5 -r 1 -t 30s --host=https://reqres.in
```

**Run with web UI:**

```bash
locust -f locustfile.py --host=https://reqres.in
```

**Open:**

👉 http://localhost:8089

Configure users and start load simulation.

**Locust reports:**

- Requests per second
- Response time distribution
- Failure rate

Uses only `GET /api/users?page=2` to stay within the 100 call/day limit.

## 🐛 Troubleshooting

### ❗ All Reqres tests failing = Cloudflare blocking

Use:

```bash
pytest tests/test_alt_api.py -v
```

### ❗ Locust port conflict

Run with another port:

```bash
locust -f locustfile.py --web-port 8090
```

### ❗ Module not found errors

```bash
pip install -r requirements.txt
```

### ❗ Connection errors

Check internet connection and verify API endpoints are accessible.

## 📞 Contact

For issues or questions:

**Name:** Nithesh Ramesh  
**Email:** nitheshrpoojari5@gmail.com

## 📝 Summary

This API Automation Suite demonstrates:

✔ Pytest + Requests automation

✔ Robust test cases (positive, negative, smoke)

✔ Graceful handling of Cloudflare blocks

✔ Backup API test suite for consistency

✔ Beautiful HTML reports

✔ Optional Locust load testing

✔ Professional structure and documentation