# tests/ui/pages/home_page.py

"""
Home page actions.

We keep these methods intentionally small. They either call BasePage.open
or navigate to specific paths so tests remain declarative and readable.
"""
from .base_page import BasePage

class HomePage(BasePage):
    SOLUTIONS_URL = "/solutions/"
    CONTACT_URL = "/contact-us/"

    def go_to_solutions(self):
        """Navigate directly to the Solutions page path."""
        # Use the base open helper for consistent URL building
        self.open(self.SOLUTIONS_URL)

    def go_to_contact(self):
        """Navigate directly to the Contact page path."""
        self.open(self.CONTACT_URL)

