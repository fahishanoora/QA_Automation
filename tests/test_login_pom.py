from pages.login_page import LoginPage

def test_valid_login(driver):

    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert "inventory.html" in driver.current_url
