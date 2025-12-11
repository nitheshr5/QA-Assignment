# 🧪 QA Automation Assignment – API & UI Test Automation Suite

This repository contains a complete end-to-end test automation project demonstrating both **API Testing** and **UI Testing**, built for a QA Automation Intern assignment.

The project is structured professionally, follows industry standards, and includes:

✔ Functional API testing

✔ Selenium UI testing with Page Object Model

✔ Load testing using Locust

✔ HTML reporting

✔ GitHub Actions CI/CD

✔ Cloudflare-handling logic (real-world consideration)

## 📁 Project Structure

```
QA-Assignment/
│
├── api-testing/                      # API Automation Module
│   ├── tests/
│   │   ├── test_reqres_api.py        # Reqres tests (auto-skip if Cloudflare)
│   │   └── test_alt_api.py           # Alternate API tests (JSONPlaceholder)
│   │
│   ├── locustfile.py                 # API Load Testing
│   ├── pytest.ini                    # Pytest markers
│   ├── requirements.txt              # API module dependencies
│   └── README.md                     # Detailed API documentation
│
├── ui-testing/                       # UI Automation Module
│   ├── tests/ui/
│   │   ├── pages/                    # Page Object Model
│   │   │   ├── base_page.py
│   │   │   ├── home_page.py
│   │   │   ├── solutions_page.py
│   │   │   └── contact_page.py
│   │   ├── conftest.py               # WebDriver setup/teardown
│   │   └── test_iamdave_ui.py        # UI test suite
│   │
│   ├── locustfile.py                 # UI Load testing
│   ├── requirements.txt              # UI module dependencies
│   └── README.md                     # Detailed UI documentation
│
├── .github/workflows/ci.yml          # Unified CI: UI + API (alternate)
│
└── README.md                         # Root documentation (this file)
```

## 🚀 Quick Start Guide

### 1️⃣ Clone the Repository

```bash
git clone <repo-url>
cd QA-Assignment
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies (per module)

**Install API dependencies:**

```bash
cd api-testing
pip install -r requirements.txt
cd ..
```

**Install UI dependencies:**

```bash
cd ui-testing
pip install -r requirements.txt
cd ..
```

## 🧰 Module 1 — API Testing

**Target API:**

- **Primary:** https://reqres.in
- **Alternate fallback:** https://jsonplaceholder.typicode.com

(Reqres is Cloudflare-protected and frequently blocks automation, so a fallback is included.)

### Key Features:

- 6+ functional test cases
- Positive, negative, and smoke tests
- Auto-skip on Cloudflare "403 Forbidden"
- Load testing with Locust
- HTML reporting
- Configurable BASE_API_URL

### Run API tests:

```bash
cd api-testing
pytest -v --html=api-report.html --self-contained-html
```

### Run only alternate tests (CI-safe):

```bash
pytest -v tests/test_alt_api.py
```

📄 **Detailed docs:** `api-testing/README.md`

## 🖥️ Module 2 — UI Testing (Selenium)

**Target Website:**

https://www.iamdave.ai

### Key Features:

- Page Object Model (POM)
- Explicit waits for reliability
- Automatic ChromeDriver management
- Headless execution for CI
- UI navigation + element validation
- HTML report output

### Run UI tests:

```bash
cd ui-testing
pytest tests/ui -v --html=ui-report.html --self-contained-html
```

📄 **Detailed docs:** `ui-testing/README.md`

## 📊 HTML Reports

Both modules produce fully self-contained HTML reports:

- `api-testing/api-report.html`
- `ui-testing/ui-report.html`

**Reports include:**

- Test summary
- Duration per test
- Environment details
- Assertions & stack traces
- Color-coded pass/fail

## 🔄 CI/CD – GitHub Actions

This project includes an automated workflow located at:

```
.github/workflows/ci.yml
```

### CI Workflow Includes:

- UI tests using headless Chromium
- API tests using JSONPlaceholder (Cloudflare-safe)
- Automatic HTML report upload
- Runs on every push & pull request to `main`

### View results:

1. Go to **Actions** tab in GitHub
2. Select the latest run
3. Download UI/API HTML report artifacts

## ⚡ Load Testing (Locust)

### API Load Test:

```bash
cd api-testing
locust -f locustfile.py --headless -u 5 -r 1 -t 30s
```

### UI Load Test:

```bash
cd ui-testing
locust -f locustfile.py
```

**Open the dashboard:**

👉 http://localhost:8089

## 🎯 Test Design Highlights

### API Testing

- pytest + requests
- Cloudflare detection → auto skip
- Positive + negative validation
- Marker-based organization
- Robust assertions

### UI Testing

- Selenium WebDriver
- Page Object Model (POM)
- Explicit waits → stable tests
- Reusable page components
- Automatic driver management

## 🐛 Real-World Considerations

| Issue | Handling |
|-------|----------|
| Cloudflare 403 on Reqres | auto-skip + alternate API |
| Dynamic UI elements | explicit waits |
| Headless browser differences | tested in CI, uses Chromium |
| Environment inconsistencies | requirements pinned per module |

## 📚 Technologies Used

| Category | Tools |
|----------|-------|
| Language | Python 3.x |
| API Testing | pytest, requests |
| UI Testing | Selenium, webdriver-manager |
| Load Testing | Locust |
| Reporting | pytest-html |
| CI/CD | GitHub Actions |

## 📝 Evaluation Criteria Coverage

This project demonstrates:

✔ Correct assertions  
✔ Positive + negative + smoke flows  
✔ Clean structure & maintainable code  
✔ Strong documentation  
✔ Automated reporting  
✔ CI/CD integration  
✔ Real API + real website testing  
✔ Professional patterns (POM, fixtures, markers)

## 📞 Contact

**Author:** Nithesh Ramesh  
**Email:** nitheshrpoojari5@gmail.com  

## ✅ Summary

This repository is a full automation framework demonstrating:

- API Testing
- UI Testing
- Load Testing
- CI/CD
- HTML reporting
- Industry-grade patterns

It is cleanly structured, well-documented, and fully production-ready.