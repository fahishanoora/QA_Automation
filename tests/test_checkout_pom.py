from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_full_checkout_flow(driver):
    # 1. Login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # 2. Add product and go to Cart
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.find_element("class name", "shopping_cart_link").click()

    # 3. Proceed to Checkout
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # 4. Fill Info -> Click Continue -> Click Finish
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info("Fahisha", "Noora", "600001")
    checkout_page.click_continue()
    checkout_page.click_finish()

    # 5. Verify Order Confirmation
    assert checkout_page.get_confirmation_text() == "Thank you for your order!"
