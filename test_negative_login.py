import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Open Chrome Browser
driver = webdriver.Chrome()
driver.maximize_window()

# 2. Go to SauceDemo Website
driver.get("https://www.saucedemo.com/")

# 3. Fill Username with VALID user, but INVALID password
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("wrong_password_123")

# 4. Click Login Button
driver.find_element(By.ID, "login-button").click()

# 5. Locate the Error Message element on the screen using XPath
time.sleep(1)
error_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
actual_error_text = error_element.text

# 6. Verify Expected Error Message matches Actual Error Message
expected_error_text = "Epic sadface: Username and password do not match any user in this service"

if expected_error_text in actual_error_text:
    print("PASS: Negative Login Test Case Passed! Error message displayed correctly.")
else:
    print("FAIL: Error message was not displayed or text did not match.")

# 7. Close Browser
driver.quit()