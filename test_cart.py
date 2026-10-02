import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Open Browser & Navigate
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# 2. Log in
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(1)

# 3. Step 1: Add Backpack to cart using XPath
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
time.sleep(1)

# 4. Step 2: Click Cart Icon using CSS Class Locator
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

# 5. Step 3: Verify Item Name in Cart using XPath
cart_item = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").text
expected_item = "Sauce Labs Backpack"

if cart_item == expected_item:
    print("PASS: Item successfully added and verified in Shopping Cart!")
else:
    print("FAIL: Item name in cart did not match expected item.")

# Clean up
driver.quit()