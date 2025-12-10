# tests/ui/pages/contact_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):

    HEADING = (By.XPATH, "//h1[contains(text(), 'Let')]")
    FORM_WRAPPER = (By.XPATH, "//div[contains(@class, 'elementor-form-fields-wrapper')]")

    def get_heading(self):
        return self.wait_for_visible(self.HEADING)

    def get_form(self):
        return self.wait_for_visible(self.FORM_WRAPPER)
