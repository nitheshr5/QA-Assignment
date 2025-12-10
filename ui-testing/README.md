# UI Testing – DaveAI Website

This module contains **Selenium-based UI automation** for the website: [https://www.iamdave.ai]

The test suite follows the **Page Object Model (POM)** design pattern for maintainability and scalability.

---

## 📋 Table of Contents

- [Test Overview](#-test-overview)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Running Tests](#-running-tests)
- [Test Reports](#-test-reports)
- [CI/CD Integration](#-cicd-integration)
- [Design Choices](#-design-choices)
- [Bonus: Load Testing](#-bonus-load-testing)

---

## 🎯 Test Overview

The test suite includes **4 comprehensive test cases** covering:

1. **Homepage Title Verification** – Validates the website loads successfully with the correct title
2. **Navigation to Solutions Page** – Tests navigation flow and verifies landing on the correct page
3. **Solutions Page CTA Demo** – Interacts with demo buttons and validates modal/form behavior
4. **Contact Page Validation** – Verifies contact page loads with expected elements

**Total Execution Time:** ~35 seconds  
**Test Results:** ✅ 4 Passed, 0 Failed

---

## 📁 Project Structure

```
ui-testing/
│
├── tests/
│   └── ui/
│       ├── pages/                    # Page Object Model (POM)
│       │   ├── base_page.py          # Base class with common methods
│       │   ├── home_page.py          # Homepage elements and actions
│       │   ├── solutions_page.py     # Solutions page elements
│       │   └── contact_page.py       # Contact page elements
│       │
│       ├── __init__.py
│       ├── conftest.py               # Pytest fixtures (setup/teardown)
│       └── test_iamdave_ui.py        # Main test cases
│
├── locustfile.py                     # Load testing script (bonus)
├── requirements.txt                  # Python dependencies
├── README.md                         # This file
└── ui-report.html                    # Generated HTML test report

```

---

## ✅ Prerequisites

Before running the tests, ensure you have:

- **Python 3.7+** installed
- **Google Chrome** browser installed
- **Internet connection** (tests run against live website)

---

## 🔧 Installation

### Step 1: Clone or Extract the Repository

```bash
cd ui-testing
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies include:**
- `pytest` – Testing framework
- `selenium` – Browser automation
- `webdriver-manager` – Automatic ChromeDriver management
- `pytest-html` – HTML report generation
- `locust` – Load testing (optional)

---

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

This creates a **standalone HTML report** (`ui-report.html`) with:
- Test execution summary
- Duration for each test
- Environment details (Python version, OS, packages)
- Pass/Fail status with color coding

### Option 3: Run a Specific Test

```bash
pytest tests/ui/test_iamdave_ui.py::test_homepage_title -v
```

---

## 📊 Test Reports

After running tests with `--html` flag, open the report:

```bash
# On Windows
start ui-report.html

# On macOS
open ui-report.html

# On Linux
xdg-open ui-report.html
```

**Sample Report Features:**
- ✅ **4 Passed** tests
- ⏱️ Execution time: ~35 seconds
- 🖥️ Environment: Python 3.12.7, Windows-10, pytest 9.0.2
- 🔌 Plugins: html, locust, metadata

---

## 🔄 CI/CD Integration

This project includes **GitHub Actions** workflow for automated testing on every push/PR.

**Workflow file:** `.github/workflows/ui-tests.yml`

**What it does:**
1. Sets up Python environment
2. Installs dependencies
3. Runs UI tests with Chrome in headless mode
4. Uploads HTML report as artifact

**To view CI results:**
- Go to **Actions** tab in GitHub repository
- Click on the latest workflow run
- Download the `ui-test-report` artifact

---

## 🎨 Design Choices

### 1. Page Object Model (POM)
**Why?**
- **Separation of Concerns:** Test logic separated from page elements
- **Reusability:** Page methods can be reused across multiple tests
- **Maintainability:** If UI changes, update only the page class, not all tests

**Example:**
```python
# home_page.py
class HomePage(BasePage):
    SOLUTIONS_LINK = (By.LINK_TEXT, "Solutions")
    
    def click_solutions(self):
        self.click(self.SOLUTIONS_LINK)

# test_iamdave_ui.py
def test_navigate_to_solutions(driver):
    home = HomePage(driver)
    home.click_solutions()
    assert "solutions" in driver.current_url
```

### 2. WebDriver Manager
**Why?**
- Automatically downloads and manages ChromeDriver
- No manual driver setup required
- Works across different OS environments

### 3. Explicit Waits
**Why?**
- Handles dynamic content loading
- More reliable than `time.sleep()`
- Prevents flaky tests due to timing issues

### 4. Fixtures in conftest.py
**Why?**
- Centralized setup/teardown for all tests
- Automatic browser cleanup after each test
- Easy to modify driver configurations (headless, window size, etc.)

---

## ⚡ Bonus: Load Testing with Locust

### What is Load Testing?
Simulates multiple users accessing the website simultaneously to test performance under load.

### Run Locust

```bash
locust -f locustfile.py --host=https://www.iamdave.ai
```

Then open browser and go to: [http://localhost:8089](http://localhost:8089)

**Configure:**
- Number of users: 10
- Spawn rate: 2 users/second

**Locust will test:**
- Homepage load time
- Solutions page load time
- Contact page load time

**View real-time stats:**
- Requests per second (RPS)
- Response times (min, max, average)
- Failure rate

---

## 🐛 Troubleshooting

### Issue: ChromeDriver not found
**Solution:** Ensure `webdriver-manager` is installed:
```bash
pip install webdriver-manager
```

### Issue: Tests fail with "element not found"
**Solution:** Increase wait time in `conftest.py`:
```python
driver.implicitly_wait(15)  # Increase from 10 to 15 seconds
```

### Issue: Browser doesn't close after test
**Solution:** The fixture handles this automatically. If it persists, check:
```python
# In conftest.py
yield driver
driver.quit()  # Ensure this line exists
```

---

## 📞 Contact

For questions or issues with the test suite, please contact:
- **Name:** Nithesh Ramesh
- **Email:** nitheshrpoojari5@gmail.com

---

## 📝 Summary

This UI test suite demonstrates:
✅ Automated browser testing with Selenium  
✅ Page Object Model design pattern  
✅ Comprehensive test coverage (navigation, interactions, validations)  
✅ HTML reporting for stakeholders  
✅ CI/CD integration with GitHub Actions  
✅ Bonus load testing capability  

**Test Execution:** Simple one-line command  
**Maintenance:** Easy to extend with new page objects  
**Reliability:** Explicit waits prevent flaky tests  
**Documentation:** Clear setup and usage instructions  

---

*Report Generated: December 10, 2025 at 17:14:54*  
*Framework: pytest-html v4.1.1*