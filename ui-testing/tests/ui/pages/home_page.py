# tests/ui/pages/home_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SOLUTIONS_URL = "/solutions/"
    CONTACT_URL = "/contact-us/"

    def go_to_solutions(self):
        self.driver.get(self.base_url + self.SOLUTIONS_URL)

    def go_to_contact(self):
        self.driver.get(self.base_url + self.CONTACT_URL)
