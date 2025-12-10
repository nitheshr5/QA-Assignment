# tests/ui/test_iamdave_ui.py

import pytest
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url)

    def go_to_solutions(self):
        self.driver.find_element(By.LINK_TEXT, "Solutions").click()

    def go_to_contact(self):
        # Some sites use "Contact" or "Contact Us" in nav
        try:
            self.driver.find_element(By.LINK_TEXT, "Contact").click()
        except Exception:
            self.driver.find_element(By.LINK_TEXT, "Contact Us").click()


@pytest.mark.ui
def test_homepage_title_contains_daveai(driver, base_url):
    """
    Verify that homepage loads successfully and title contains 'DaveAI'.
    """
    home = HomePage(driver, base_url)
    home.open()

    title = driver.title
    assert "DaveAI" in title, f"Expected 'DaveAI' in page title, got: {title!r}"


@pytest.mark.ui
def test_navigation_to_solutions_page(driver, base_url):
    """
    Click on 'Solutions' in the navbar and verify that:
    - URL contains '/solutions'
    - H1 heading contains either 'Solutions' or the known marketing heading
      'Enhance Sales Exponentially'.
    """
    home = HomePage(driver, base_url)
    home.open()
    home.go_to_solutions()

    current_url = driver.current_url
    assert "solutions" in current_url.lower(), f"Expected to be on Solutions page, got: {current_url}"

    heading = driver.find_element(By.TAG_NAME, "h1")
    text = heading.text.strip()

    assert ("Solutions" in text) or ("Enhance Sales Exponentially" in text), (
        f"Unexpected Solutions page heading: {text!r}"
    )


@pytest.mark.ui
def test_solutions_page_has_demo_cta(driver, base_url):
    """
    On Solutions page, ensure there is a clear call-to-action button
    such as 'Book Demo' or 'Get a Free Demo'.
    """
    home = HomePage(driver, base_url)
    home.open()
    home.go_to_solutions()

    cta = driver.find_element(
        By.XPATH,
        "//a[contains(., 'Book Demo') or contains(., 'Get a Free Demo')]"
    )
    assert cta.is_displayed(), "CTA button for demo should be visible on Solutions page"


@pytest.mark.ui
def test_contact_page_has_contact_section(driver, base_url):
    """
    Navigate to Contact page and verify:
    - URL contains 'contact'
    - A heading / text with 'Let’s Discuss Your Growth Goals' or 'Get in touch' exists
    - This ensures the main contact form section is present.
    """
    home = HomePage(driver, base_url)
    home.open()
    home.go_to_contact()

    current_url = driver.current_url.lower()
    assert "contact" in current_url, f"Expected contact page, got: {current_url}"

    # Main heading
    h1 = driver.find_element(By.TAG_NAME, "h1")
    h1_text = h1.text.strip()

    # On their contact page they highlight 'Let’s Discuss Your Growth Goals'. :contentReference[oaicite:5]{index=5}
    assert ("Discuss Your Growth Goals" in h1_text) or ("Contact" in h1_text), (
        f"Unexpected contact page heading: {h1_text!r}"
    )

    # Check a supporting 'Get in touch' text or similar section is visible. :contentReference[oaicite:6]{index=6}
    get_in_touch = driver.find_element(
        By.XPATH,
        "//*[contains(translate(text(), 'GET IN TOUCH', 'get in touch'), 'get in touch')]"
    )
    assert get_in_touch.is_displayed(), "'Get in touch' section should be visible on contact page"
