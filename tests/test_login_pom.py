import logging
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)

def test_valid_login(driver):
    logger.info("Starting valid login test...")

    login_page = LoginPage(driver)

    logger.info("Navigating to Saucedemo login page")
    login_page.open_page()

    logger.info("Entering credentials for standard_user")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")

    logger.info("Clicking login button")
    login_page.click_login()

    logger.info("Verifying redirection to inventory page")
    assert "inventory.html" in driver.current_url
