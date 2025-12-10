

import pytest
from tests.ui.pages.home_page import HomePage
from tests.ui.pages.solutions_page import SolutionsPage
from tests.ui.pages.contact_page import ContactPage


@pytest.mark.ui
def test_homepage_title(driver, base_url):
    driver.get(base_url)
    assert "DaveAI" in driver.title


@pytest.mark.ui
def test_navigate_to_solutions(driver, base_url):
    home = HomePage(driver, base_url)
    home.go_to_solutions()

    solutions = SolutionsPage(driver, base_url)
    heading = solutions.get_heading().text.lower()
    assert "solutions" in heading or "sales" in heading


@pytest.mark.ui
def test_solutions_demo_cta(driver, base_url):
    home = HomePage(driver, base_url)
    home.go_to_solutions()

    solutions = SolutionsPage(driver, base_url)
    cta = solutions.get_cta_button()

    assert cta.is_displayed()


@pytest.mark.ui
def test_contact_page(driver, base_url):
    home = HomePage(driver, base_url)
    home.go_to_contact()

    contact = ContactPage(driver, base_url)

    assert contact.get_heading().is_displayed()
    assert contact.get_form().is_displayed()
