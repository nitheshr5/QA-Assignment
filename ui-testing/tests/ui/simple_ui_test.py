#tests/simple_ui_test.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

#open application URL
driver.get("https://www.iamdave.ai")

# Test case 1: verify Home Page Title
print("Running Test Case Verify Home Page Title")

title = driver.title
assert "Dave" in title or "DaveAI" in title, f"Unexpected title: {title}"
print("Home page title verified successfully")

# Test case 2: navigate to solutions Page 
print("Running Test Case: Navigate to Solutions Page")

driver.get("https://www.iamdave.ai/solutions/")
time.sleep(3)

heading = driver.find_element(By.TAG_NAME, "h1").text.lower()
assert "solutions" in heading or "sales" in heading, f"Unexpected heading: {heading}"
print("Solutions page navigation verified")

# Test case 3: verify Book Demo CTA 
print("Running Test Case: Verify Book Demo CTA")

cta_button = driver.find_element(
    By.XPATH, "//a[contains(@class, 'elementor-button') and contains(., 'Book Demo')]"
)
assert cta_button.is_displayed(), "Book Demo CTA is not visible"
print("CTA button is visible")

#  Test case 4: navigate to ContactPage 
print("running testcase: navigate to contactpage")

driver.get("https://www.iamdave.ai/contact-us/")
time.sleep(3)

contact_heading = driver.find_element(By.TAG_NAME, "h1")
assert contact_heading.is_displayed(), "contactpage heading not visible"

contact_form = driver.find_element(
    By.XPATH, "//div[contains(@class, 'elementor-form') or contains(@class, 'wpcf7-form')]"
)
assert contact_form.is_displayed(), "contact form not visible"

print("contact page verified successfully")

# close browser
driver.quit()
print("All tests case passed")
