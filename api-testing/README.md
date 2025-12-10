# 📘 API Testing – Reqres Demo (QA Automation Assignment)

This folder contains the **API automation** part of the QA Automation Intern Assignment.

The purpose of this module is to demonstrate:
- Functional API testing using `pytest` + `requests`
- Positive, negative, and smoke test design
- Basic load testing using `Locust`
- Handling real-world issues such as rate limits & Cloudflare blocking
- How to structure, run, mock, and report API automation tests professionally

---

## 📁 Folder Structure

```
api-testing/
│
├── tests/
│   └── test_reqres_api.py         # API tests for Reqres
│
├── locustfile.py                  # Load test for GET /users?page=2
├── pytest.ini                     # Pytest marker configuration
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## 🛠️ 1. Setup Instructions

### 1.1 Create and activate a virtual environment (from project root)

```bash
python -m venv venv

# Windows PowerShell:
venv\Scripts\activate

# Git Bash / macOS / Linux:
source venv/Scripts/activate
```

### 1.2 Install API test dependencies

```bash
cd api-testing
pip install -r requirements.txt
```

**Dependencies include:**
- `pytest` – Testing framework
- `requests` – HTTP library for API calls
- `locust` – Load testing framework
- `pytest-html` – HTML report generation

---

## ▶️ 2. Running the Pytest Suite

All API tests live in `tests/test_reqres_api.py`.

### 2.1 Run all API tests

```bash
pytest -v -m api
```

### 2.2 Run only smoke tests

```bash
pytest -v -m smoke
```

### 2.3 Run only positive or negative scenarios

```bash
# Positive test cases (valid workflows)
pytest -v -m positive

# Negative test cases (error handling)
pytest -v -m negative
```

**Markers are defined in `pytest.ini`:**

```ini
[pytest]
markers =
    api: API tests for Reqres
    positive: Valid workflow test cases
    negative: Error-handling test cases
    smoke: Minimal set of tests for quick verification
```

---

## 📊 3. Generating Test Reports

### Generate HTML Report (recommended)

```bash
pytest -v -m api --html=api-report.html --self-contained-html
```

**Output:**
```
api-testing/api-report.html
```

Open it in a browser for a fully styled test report with:
- ✅ Pass/Fail summary
- ⏱️ Test duration
- 📋 Environment details
- 🔍 Detailed assertions

**To open the report:**

```bash
# On Windows
start api-report.html

# On macOS
open api-report.html

# On Linux
xdg-open api-report.html
```

---

## ✔️ 4. Test Case Design Summary

### 📗 Positive Tests

| Test Case | Endpoint | Validation |
|-----------|----------|------------|
| **List Users** | `GET /users?page=2` | Returns 200 and non-empty user list |
| **Get Single User** | `GET /users/2` | Returns user with `id = 2` |
| **Create User** | `POST /users` | Returns 201 + `createdAt` + `id` |
| **Register User** | `POST /register` | Valid credentials return `id` + `token` |

### 📕 Negative Tests

| Test Case | Endpoint | Expected Result |
|-----------|----------|-----------------|
| **Non-existing User** | `GET /users/23` | Returns 404 |
| **Register Without Password** | `POST /register` | Returns 400 + "Missing password" error |

### What Each Test Checks:
✅ **HTTP status codes** (200, 201, 400, 404)  
✅ **Required JSON fields** (id, email, createdAt, token)  
✅ **Error messages** (proper error handling)  
✅ **Correct data types** (strings, integers, timestamps)  

All tests use **realistic browser-like headers** to simulate a genuine client and avoid detection as a bot.

---

## ⚙️ 5. Load Testing With Locust (Optional Bonus)

This project includes a lightweight Locust test (`locustfile.py`) that safely stays within the assignment limit of **< 100 API calls/day**.

### Run in headless mode:

```bash
locust -f locustfile.py --headless -u 5 -r 1 -t 30s --host https://reqres.in
```

### Parameters:

| Param | Meaning |
|-------|---------|
| `-u 5` | 5 concurrent simulated users |
| `-t 30s` | Run for 30 seconds |
| `-r 1` | Spawn rate = 1 user/sec |
| `--headless` | No UI, quick CLI run |

### Locust automatically reports:
- 📊 Request count
- ⚡ RPS (requests per second)
- ❌ Failure rate
- ⏱️ Response times (min/avg/max)

### Run with Web UI (Interactive Dashboard):

```bash
locust -f locustfile.py --host https://reqres.in
```

Then open: [http://localhost:8089](http://localhost:8089)

Configure users and spawn rate through the web interface, then click "Start Swarming" to begin the load test.

---

## 🚧 6. Cloudflare "403 Forbidden" Issue (Important)

Because **Reqres.in** is protected by **Cloudflare**, automated traffic from Python, Postman, or certain networks may be blocked with a **403 Forbidden** HTML challenge page:

```html
<title>Just a moment...</title>
```

This is **expected behavior** of Cloudflare's bot protection.

### Why this happens:

❌ **Python requests** does NOT execute JavaScript → cannot pass Cloudflare challenge  
❌ **Postman** also cannot pass Cloudflare → also blocked  
❌ **Some networks** (VPNs, corporate IPs) trigger stricter rules  

✅ **Browser works** because it:
- Runs JavaScript
- Sets Cloudflare cookies
- Responds to JS challenges
- Sends complex browser fingerprints

**This issue is environmental, not test-code related.**

### How this project handles it:

Each test implements a helper function:

```python
def skip_if_forbidden(response):
    if response.status_code == 403:
        pytest.skip("Cloudflare blocked the request with 403 Forbidden.")
```

**Tests will:**
- ✔ Run fully when Reqres is accessible
- ✔ Auto-skip when Cloudflare blocks the request
- ❌ Never falsely fail because of an external service outage

### Sample Output When Blocked:

```
tests/test_reqres_api.py::test_get_list_users SKIPPED (Cloudflare blocked...)
tests/test_reqres_api.py::test_get_single_user SKIPPED (Cloudflare blocked...)
```

---

## 🐛 Troubleshooting

### Issue: All tests are skipped with 403 errors

**Cause:** Cloudflare is blocking automated requests  
**Solutions:**
1. Try running tests from a different network (home vs corporate)
2. Disable VPN if using one
3. Wait a few minutes and retry (rate limiting may reset)
4. Use a different testing API (e.g., JSONPlaceholder) if Cloudflare persists

### Issue: `ModuleNotFoundError: No module named 'pytest'`

**Solution:** Ensure you're in the virtual environment and installed dependencies:
```bash
source venv/Scripts/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: Locust doesn't start

**Solution:** Check if port 8089 is already in use:
```bash
# Kill existing Locust processes
pkill -f locust

# Or specify a different port
locust -f locustfile.py --web-port 8090
```

---

## 📝 Summary

This API test suite demonstrates:

✅ **RESTful API testing** with Python + pytest  
✅ **Comprehensive test coverage** (positive, negative, smoke tests)  
✅ **Professional test markers** for flexible execution  
✅ **Multiple report formats** (HTML, XML, Allure)  
✅ **Load testing capability** with Locust  
✅ **Real-world issue handling** (Cloudflare, rate limits)  
✅ **Clean code structure** with reusable patterns  
✅ **Clear documentation** for easy onboarding  

**Test Execution:** Simple marker-based commands  
**Reporting:** Production-ready HTML reports  
**Resilience:** Graceful handling of external service issues  
**Scalability:** Easy to extend with new test cases  

---

## 📞 Contact

For questions or issues with the test suite, please contact:
- **Name:** Nithesh Ramesh
- **Email:** nitheshrpoojari5@gmail.com

---

*API Testing Framework for QA Automation Intern Assignment*  
*Tested Against: https://reqres.in*  
*Framework: pytest + requests + locust*