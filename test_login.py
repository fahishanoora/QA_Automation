import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Open Chrome Browser
driver = webdriver.Chrome()
driver.maximize_window()

# 2. Go to SauceDemo Website
driver.get("https://www.saucedemo.com/")

# 3. Fill Username & Password
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# 4. Click Login Button
driver.find_element(By.ID, "login-button").click()

# 5. Check if Login Succeeded
time.sleep(2)
if "inventory.html" in driver.current_url:
    print("PASS: Login Test Case Executed Successfully!")
else:
    print("FAIL: Login Failed.")

# 6. Close Browser
driver.quit()