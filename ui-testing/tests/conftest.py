"""
Pytest fixtures for UI tests.

- driver: creates a Chrome WebDriver using webdriver-manager.
- base_url: can be overridden with the BASE_URL environment variable.
- HEADLESS behavior can be toggled with HEADLESS env var (default is true).
"""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def base_url():
# Make it easy to override in CI or locally: export BASE_URL="https://staging.iamdave.ai"
    return os.environ.get("BASE_URL", "https://www.iamdave.ai")


@pytest.fixture
def driver():
    """
    Instantiate Chrome WebDriver.

    Environment variables:
    - HEADLESS (true/false) to toggle headless mode. Default: true.
    """
    headless_env = os.environ.get("HEADLESS", "true").lower()
    headless = headless_env not in ("0", "false", "no")

    options = webdriver.ChromeOptions()
    # when headless is requested, use the modern headless flag
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    # Helpful flags for CI / Docker environments
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")  # harmless even if not used

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # A modest implicit wait helps with simple timing issues; explicit waits are used in pages.
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
