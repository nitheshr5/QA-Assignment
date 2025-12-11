# tests/ui/pages/contact_page.py

"""
Contact page object with locators for the heading and the contact form area.
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):
    # Locator picks up headings that start with words like 'Let...' (e.g., 'Let's talk')
    HEADING = (By.XPATH, "//h1[contains(normalize-space(.), \"Let\")]")
    FORM_WRAPPER = (By.XPATH, "//div[contains(@class, 'elementor-form-fields-wrapper') or contains(@class, 'wpcf7-form')]")

    def get_heading(self):
        return self.wait_for_visible(self.HEADING)

    def get_form(self):
        return self.wait_for_visible(self.FORM_WRAPPER)
