import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Open Browser & Navigate
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Smart Wait Setup (10 seconds timeout)
wait = WebDriverWait(driver, 10)

# 2. Log in
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# 3. Add Item to Cart
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"))).click()

# 4. Open Cart
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

# 5. Click Checkout Button
wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

# 6. Fill Out Shipping Information Form
first_name = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
first_name.send_keys("Aisha")
driver.find_element(By.ID, "last-name").send_keys("Khan")
driver.find_element(By.ID, "postal-code").send_keys("00000")

# 7. Click Continue
driver.find_element(By.ID, "continue").click()

# 8. Click Finish to Complete Order
wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

# 9. Verify Order Confirmation Header
header_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[@class='complete-header']")))
confirmation_header = header_element.text
expected_header = "THANK YOU FOR YOUR ORDER"  # SauceDemo uses uppercase in page content

if "THANK YOU" in confirmation_header.upper():
    print("PASS: Full End-to-End Checkout Test Executed Successfully!")
else:
    print(f"FAIL: Found header text '{confirmation_header}' instead of expected.")

# Clean up
driver.quit()