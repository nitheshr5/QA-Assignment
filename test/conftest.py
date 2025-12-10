# tests/conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def base_url():
    return "https://www.iamdave.ai"


@pytest.fixture
def driver():
    """
    Creates a new Chrome browser for each test and quits after.
    Headless mode so it can run in CI or without opening a window.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Headless Chrome
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(10)
    yield driver
    driver.quit()
