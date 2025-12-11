# 🌐 UI Testing – DaveAI Website

This module contains the Selenium-based UI automation suite for the website:

👉 https://www.iamdave.ai

The tests follow the **Page Object Model (POM)** pattern to ensure clarity, reusability, and easy scalability as the website grows.

## 📋 Table of Contents

1. [Overview](#-overview)
2. [Project Structure](#-project-structure)
3. [Prerequisites](#-prerequisites)
4. [Installation](#-installation)
5. [Running Tests](#-running-tests)
6. [HTML Reports](#-html-reports)
7. [Design Choices](#-design-choices)
8. [Bonus: Load Testing](#-bonus-load-testing)
9. [Troubleshooting](#-troubleshooting)
10. [Contact](#-contact)
11. [Summary](#-summary)

## 🎯 Overview

This UI test suite automates essential user flows on the live DaveAI website.

### ✔ Current Test Coverage

- Homepage Title Verification
- Navigation to Solutions Page
- Solutions Page CTA Visibility
- Contact Page Load & Form Visibility

All tests use **Selenium + Pytest + Page Objects** for clean separation of concerns.

**Average execution time:** 30–40 seconds

## 📁 Project Structure

```
ui-testing/
│
├── tests/
│   └── ui/
│       ├── pages/
│       │   ├── base_page.py         # Common helpers/waits
│       │   ├── home_page.py         # Homepage object
│       │   ├── solutions_page.py    # Solutions page object
│       │   └── contact_page.py      # Contact page object
│       │
│       ├── conftest.py              # WebDriver fixtures
│       └── test_iamdave_ui.py       # Main UI test suite
│
├── locustfile.py                    # Optional load testing
├── requirements.txt
└── README.md
```

## ✅ Prerequisites

Before running the UI tests, ensure you have:

- **Python 3.7+**
- **Google Chrome** installed
- **Internet connection** (tests run against the live site)

## 🔧 Installation

From the project root:

```bash
cd ui-testing
pip install -r requirements.txt
```

### Key dependencies

- selenium
- pytest
- webdriver-manager
- pytest-html
- locust (optional)

## 🚀 Running Tests

### Option 1: Run All UI Tests (Verbose Output)

```bash
pytest tests/ui -v
```

**Expected Output:**

```
tests/ui/test_iamdave_ui.py::test_homepage_title PASSED
tests/ui/test_iamdave_ui.py::test_navigate_to_solutions PASSED
tests/ui/test_iamdave_ui.py::test_solutions_demo_cta PASSED
tests/ui/test_iamdave_ui.py::test_contact_page PASSED

====== 4 passed in 35.12s ======
```

### Option 2: Generate HTML Report

```bash
pytest tests/ui -v --html=ui-report.html --self-contained-html
```

This generates a standalone HTML report (`ui-report.html`) containing:

- Execution summary
- Test duration
- Browser & environment details
- Colored pass/fail results

### Option 3: Run a Specific Test

```bash
pytest tests/ui/test_iamdave_ui.py::test_homepage_title -v
```

### Option 4: Run Tests Without Headless Mode (Debugging)

```bash
# Linux / macOS:
export HEADLESS=false

# Windows PowerShell:
$env:HEADLESS = "false"

pytest tests/ui -v
```

## 📊 HTML Reports

To open the generated HTML report:

```bash
# Windows
start ui-report.html

# macOS
open ui-report.html

# Linux
xdg-open ui-report.html
```

HTML report includes:

- Test results
- Execution environment
- Traceback for failures
- Clean visual separation of each test

## 🎨 Design Choices

### 1. Page Object Model (POM)

Organizes code into:

- **Page classes** → define elements & actions
- **Tests** → focus only on verifications

This makes tests readable and easy to extend.

### 2. Explicit Waits

All page objects use:

```python
wait_for_visible(locator)
```

to avoid flakiness due to slow or dynamic elements.

### 3. WebDriver Fixtures (conftest.py)

Handles:

- Browser setup
- Headless mode
- Window sizing
- Cleanup automatically

### 4. WebDriver Manager

Automatically downloads correct ChromeDriver → No manual setup required.

## ⚡ Bonus: Load Testing

A small Locust script is included to measure response performance of:

- Homepage
- Solutions Page
- Contact Page

**Run Locust:**

```bash
locust -f locustfile.py --host=https://www.iamdave.ai
```

**Open:**

👉 http://localhost:8089

Configure users and start load simulation.

**Locust reports:**

- Requests per second
- Response time distribution
- Failure rate

## 🐛 Troubleshooting

### ❗ ChromeDriver not found

```bash
pip install webdriver-manager
```

### ❗ Elements not found / flaky tests

Increase wait time:

```python
driver.implicitly_wait(10)
```

### ❗ Website looks different in headless mode

Run non-headless:

```bash
HEADLESS=false pytest -v
```

### ❗ Browser does not close

Ensure this line exists in `conftest.py`:

```python
driver.quit()
```

## 📞 Contact

For issues or questions:

**Name:** Nithesh Ramesh  
**Email:** nitheshrpoojari5@gmail.com

## 📝 Summary

This UI Automation Suite demonstrates:

✔ Selenium + Pytest automation

✔ Clean Page Object Model

✔ Reliable navigation & UI validation tests

✔ Beautiful HTML reports

✔ Optional Locust load testing

✔ Easy-to-maintain structure