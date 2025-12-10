# 🧪 QA Automation Assignment – API & UI Testing

This repository contains a comprehensive test automation suite demonstrating both **API testing** and **UI testing** capabilities for a QA Automation Intern Assignment.

---

## 📋 Assignment Overview

This project includes two major testing components:

1. **API Testing** – Automated functional and load testing for [Reqres.in](https://reqres.in) API
2. **UI Testing** – Selenium-based browser automation for [www.iamdave.ai](https://www.iamdave.ai)

Both modules follow industry best practices including:
- Clean code structure with design patterns (Page Object Model)
- Comprehensive test coverage (positive, negative, smoke tests)
- HTML report generation for stakeholder visibility
- CI/CD integration with GitHub Actions
- Real-world issue handling (Cloudflare blocking, dynamic content)

---

## 📁 Project Structure

```
qa-automation-assignment/
│
├── api-testing/                    # API automation module
│   ├── tests/
│   │   └── test_reqres_api.py
│   ├── locustfile.py              # Load testing
│   ├── pytest.ini
│   ├── requirements.txt
│   └── README.md                  # Detailed API testing docs
│
├── ui-testing/                     # UI automation module
│   ├── tests/
│   │   └── ui/
│   │       ├── pages/             # Page Object Model
│   │       ├── conftest.py
│   │       └── test_iamdave_ui.py
│   ├── locustfile.py              # Load testing
│   ├── requirements.txt
│   └── README.md                  # Detailed UI testing docs
│
├── .github/
│   └── workflows/
│       ├── api-tests.yml          # CI/CD for API tests
│       └── ui-tests.yml           # CI/CD for UI tests
│
└── README.md                       # This file
```

---

## 🚀 Quick Start Guide

### Prerequisites

- **Python 3.7+** installed
- **Google Chrome** browser (for UI tests)
- **Internet connection** (tests run against live services)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd qa-automation-assignment
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies for each module**
   ```bash
   # API Testing
   cd api-testing
   pip install -r requirements.txt
   cd ..
   
   # UI Testing
   cd ui-testing
   pip install -r requirements.txt
   cd ..
   ```

---

## 📦 Module 1: API Testing

**Target:** [Reqres.in](https://reqres.in) REST API

### Key Features
- ✅ 6 test cases covering GET, POST endpoints
- ✅ Positive and negative test scenarios
- ✅ Cloudflare blocking detection and handling
- ✅ Load testing with Locust
- ✅ Marker-based test execution (smoke, positive, negative)

### Quick Run
```bash
cd api-testing
pytest -v -m api --html=api-report.html --self-contained-html
```

### What's Tested
- List users pagination
- Single user retrieval
- User creation
- User registration (success & failure scenarios)
- 404 error handling
- 400 bad request validation

📖 **For detailed instructions, see:** [`api-testing/README.md`](api-testing/README.md)

---

## 🖥️ Module 2: UI Testing

**Target:** [www.iamdave.ai](https://www.iamdave.ai)

### Key Features
- ✅ 4 comprehensive UI test cases
- ✅ Page Object Model (POM) design pattern
- ✅ Explicit waits for dynamic content
- ✅ Automated ChromeDriver management
- ✅ HTML report with test execution details
- ✅ Load testing with Locust

### Quick Run
```bash
cd ui-testing
pytest tests/ui -v --html=ui-report.html --self-contained-html
```

### What's Tested
- Homepage title verification
- Navigation flow (Solutions page)
- Interactive elements (CTA buttons, modals)
- Contact page validation
- Form field presence

📖 **For detailed instructions, see:** [`ui-testing/README.md`](ui-testing/README.md)

---

## 📊 Test Reports

Both modules generate **standalone HTML reports** that can be opened in any browser:

```bash
# API Testing Report
api-testing/api-report.html

# UI Testing Report
ui-testing/ui-report.html
```

**Reports include:**
- ✅ Pass/Fail summary with color coding
- ⏱️ Execution time for each test
- 🖥️ Environment details (Python version, OS, packages)
- 📋 Detailed assertion results
- ❌ Error messages and stack traces (if any)

---

## 🔄 CI/CD Integration

This project includes **GitHub Actions** workflows for automated testing:

### API Tests Workflow
- Triggers on push/pull request to `main` branch
- Runs all API tests with markers
- Uploads HTML report as artifact
- Location: `.github/workflows/api-tests.yml`

### UI Tests Workflow
- Triggers on push/pull request to `main` branch
- Runs UI tests in headless Chrome
- Uploads HTML report as artifact
- Location: `.github/workflows/ui-tests.yml`

**View Results:**
1. Go to **Actions** tab in GitHub
2. Click on the latest workflow run
3. Download artifacts to view reports

---

## ⚡ Bonus: Load Testing

Both modules include **Locust** scripts for performance testing:

### API Load Test
```bash
cd api-testing
locust -f locustfile.py --headless -u 5 -r 1 -t 30s --host https://reqres.in
```

### UI Load Test
```bash
cd ui-testing
locust -f locustfile.py --host https://www.iamdave.ai
```

Then open: [http://localhost:8089](http://localhost:8089) for interactive dashboard.

---

## 🎯 Test Design Highlights

### API Testing
- **Framework:** pytest + requests
- **Approach:** Marker-based execution (smoke, positive, negative)
- **Challenge Handling:** Cloudflare 403 blocking with auto-skip
- **Best Practice:** Realistic browser headers, proper status code validation

### UI Testing
- **Framework:** Selenium + pytest
- **Design Pattern:** Page Object Model (POM)
- **Wait Strategy:** Explicit waits for reliability
- **Best Practice:** Centralized fixtures, reusable page methods

---

## 🐛 Known Issues & Solutions

### Cloudflare 403 Blocking (API Tests)
**Issue:** Reqres.in may block automated requests  
**Solution:** Tests auto-skip with clear message when blocked  
**Workaround:** Try different network or disable VPN

### Element Not Found (UI Tests)
**Issue:** Dynamic content not loaded in time  
**Solution:** Explicit waits implemented in all page objects  
**Adjustment:** Increase wait time in `conftest.py` if needed

---

## 📚 Technologies Used

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | Python 3.12+ | Test automation scripting |
| **API Testing** | pytest, requests | Functional API testing |
| **UI Testing** | Selenium WebDriver | Browser automation |
| **Design Pattern** | Page Object Model | UI test maintainability |
| **Load Testing** | Locust | Performance testing |
| **Reporting** | pytest-html | HTML test reports |
| **CI/CD** | GitHub Actions | Automated test execution |
| **Driver Management** | webdriver-manager | ChromeDriver auto-setup |

---

## ✅ Evaluation Criteria Checklist

This project demonstrates:

- ✅ **Correctness** – All assertions validate expected behavior
- ✅ **Usefulness** – Tests cover critical user flows and edge cases
- ✅ **Code Quality** – Clean, readable, well-commented code
- ✅ **API Automation** – Functional and load testing with pytest + requests
- ✅ **UI Automation** – Selenium with POM design pattern
- ✅ **Documentation** – Clear setup, execution, and teardown steps
- ✅ **Best Practices** – Fixtures, markers, explicit waits, error handling
- ✅ **Professional Structure** – Modular design with separate concerns

---

## 📞 Contact

**Author:** Nithesh Ramesh  
**Email:** nitheshrpoojari5@gmail.com 
**LinkedIn:** [Your LinkedIn Profile]

---

## 📝 Summary

This repository showcases a **production-ready test automation framework** with:

🎯 **Comprehensive Coverage** – Both API and UI testing in one project  
🏗️ **Professional Structure** – Clean architecture with design patterns  
📊 **Visual Reports** – Stakeholder-friendly HTML reports  
🔄 **CI/CD Ready** – GitHub Actions integration  
⚡ **Performance Testing** – Locust load testing capability  
🛡️ **Resilient** – Handles real-world issues gracefully  
📖 **Well-Documented** – Clear instructions for easy setup  



---

*QA Automation Assignment – Demonstrating End-to-End Testing Capabilities*