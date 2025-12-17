# tests/ui//base_page.py
"""
UI smoke tests for iamdave.ai

These tests use the small page-object layer in tests/ui/pages/ to keep assertions
readable and to demonstrate simple navigation / verification flows.

Markers:
- @pytest.mark.ui : mark these as UI tests (so you can run them separately)
"""
import pytest
from tests.ui.pages.home_page import HomePage
from tests.ui.pages.solutions_page import SolutionsPage
from tests.ui.pages.contact_page import ContactPage


@pytest.mark.ui
def test_homepage_title(driver, base_url):
    """
    Verify the site loads and the browser title contains an expected brand string.
    This is a quick sanity/smoke check.
    """
    # Use the page object for consistency
    home = HomePage(driver, base_url)
    home.open()  # opens base_url
    assert "DaveAI" in driver.title or "Dave" in driver.title, f"Unexpected title: {driver.title}"


@pytest.mark.ui
def test_navigate_to_solutions(driver, base_url):
    """
    Navigate from the home page to the Solutions page and verify heading text.
    The assertion allows either 'solutions' or 'sales' because some sites use different headings.
    """
    home = HomePage(driver, base_url)
    home.open()
    home.go_to_solutions()

    solutions = SolutionsPage(driver, base_url)
    heading_text = solutions.get_heading().text.strip().lower()
    assert "solutions" in heading_text or "sales" in heading_text, (
        f"Unexpected solutions heading: {heading_text}"
    )


@pytest.mark.ui
def test_solutions_demo_cta(driver, base_url):
    """
    Verify the 'Book Demo' (CTA) button is present and visible on the Solutions page.
    This checks a core business action is available to users.
    """
    home = HomePage(driver, base_url)
    home.open()
    home.go_to_solutions()

    solutions = SolutionsPage(driver, base_url)
    cta = solutions.get_cta_button()
    assert cta.is_displayed(), "CTA button should be visible on the Solutions page"


@pytest.mark.ui
def test_contact_page(driver, base_url):
    """
    Navigate to the contact page and verify the main heading and contact form exist.
    """
    home = HomePage(driver, base_url)
    home.open()
    home.go_to_contact()

    contact = ContactPage(driver, base_url)
    assert contact.get_heading().is_displayed(), "Contact page heading should be visible"
    assert contact.get_form().is_displayed(), "Contact form should be visible on contact page"
