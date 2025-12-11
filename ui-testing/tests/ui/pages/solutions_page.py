# tests/ui/pages/solutions_page.py

"""
Solutions page object containing key locators and helpers.
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage

class SolutionsPage(BasePage):
    CTA = (By.XPATH, "//a[contains(@class, 'elementor-button') and contains(., 'Book Demo')]")
    HEADING = (By.TAG_NAME, "h1")

    def get_heading(self):
        """Return the main heading element (waits until visible)."""
        return self.wait_for_visible(self.HEADING)

    def get_cta_button(self):
        """Return the primary CTA button element."""
        return self.wait_for_visible(self.CTA)

