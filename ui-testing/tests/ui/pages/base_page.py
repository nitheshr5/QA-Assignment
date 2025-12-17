# tests/ui/pages/base_page.py

"""
Small base page abstraction using explicit waits.

Contains common helpers used by page objects.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_url=None, timeout: int = 10):
        self.driver = driver
        self.base_url = base_url or ""  
        self.wait = WebDriverWait(driver, timeout)

    def open(self, path: str = ""):
        """Open a page given a path relative to base_url (base_url must include scheme)."""
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}" if path else self.base_url
        self.driver.get(url)

    def wait_for_visible(self, locator):
        """Wait until the locator is visible and return the WebElement."""
        return self.wait.until(EC.visibility_of_element_located(locator))
