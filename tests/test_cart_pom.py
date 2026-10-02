from pages.login_page import LoginPage
from pages.cart_page import CartPage

def test_add_to_cart_and_checkout(driver):

    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.find_element("class name", "shopping_cart_link").click()

    cart_page = CartPage(driver)
    assert cart_page.get_cart_item_name() == "Sauce Labs Backpack"
    cart_page.click_checkout()

    assert "checkout-step-one.html" in driver.current_url