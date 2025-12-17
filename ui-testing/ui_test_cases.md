# UI Test Cases – iamdave.ai

## Application Under Test
- URL: https://www.iamdave.ai
- Browser: Google Chrome

---

## Ui test cases 1 – Verify Home Page Title

### Objective
To verify that the iamdave.ai home page loads successfully and displays the correct browser title.

### Preconditions
- Chrome browser is installed
- Internet connection is available

### Test Steps
1. Open Chrome browser
2. Navigate to https://www.iamdave.ai
3. Capture the browser title

### Expected Result
- Home page should load successfully
- Browser title should contain **"Dave"** or **"DaveAI"**

---

## Ui test case 2 – Verify Navigation to Solutions Page

### Objective
To verify that the user can navigate to the Solutions page.

### Test Steps
1. Open browser
2. Navigate to https://www.iamdave.ai
3. Open the Solutions page
4. Observe the page heading

### Expected Result
- Solutions page should open successfully
- Page heading should contain **"Solutions"** or **"Sales"**

---

## Ui test case 3 – Verify Book Demo CTA on Solutions Page

### Objective
To verify that the **Book Demo** call-to-action button is visible on the Solutions page.

### Test Steps
1. Navigate to the Solutions page
2. Locate the **Book Demo** button
3. Check button visibility

### Expected Result
- Book Demo button should be visible and accessible to the user

---

## Ui test case 4 – Verify Contact Page and Contact Form

### Objective
To verify that the Contact page opens successfully and displays the contact form.

### Test Steps
1. Navigate to the Contact page
2. Verify the page heading
3. Verify the contact form section

### Expected Result
- Contact page heading should be visible
- Contact form should be displayed correctly

---

## Notes
- These test cases are automated using **Selenium with Python**
- Each test case is mapped directly to automation steps in `simple_ui_test.py`
- Tests are designed as **smoke-level UI validations**
