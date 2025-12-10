# tests/ui/pages/solutions_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage

class SolutionsPage(BasePage):

    CTA = (By.XPATH, "//a[contains(@class, 'elementor-button') and contains(., 'Book Demo')]")
    HEADING = (By.TAG_NAME, "h1")

    def get_heading(self):
        return self.wait_for_visible(self.HEADING)

    def get_cta_button(self):
        return self.wait_for_visible(self.CTA)
