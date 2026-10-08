import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected_error", [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),  # <--- Restored
    ("invalid_user", "wrong_pass", "Epic sadface: Username and password do not match any user in this service"),
    ("", "secret_sauce", "Epic sadface: Username is required")
])
def test_invalid_login_scenarios(driver, username, password, expected_error):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    actual_error = login_page.get_error_message()
    assert expected_error in actual_error