from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

driver.maximize_window()

time.sleep(3)

username = driver.find_element(By.XPATH, '//input[contains(@id, "username")]')
username.click()
username.send_keys("wrong_user")

time.sleep(3)

password = driver.find_element(By.XPATH, '//input[contains(@id, "password")]')
password.click()
password.send_keys("wrong_pass")

time.sleep(3)

login_button = driver.find_element(By.XPATH, '//button[contains(@type, "submit")]')
login_button.click()

time.sleep(3)

error_message = driver.find_element(By.XPATH, '//div[contains(@id, "flash")]')
print(error_message.text)
assert "Your username is invalid!" in error_message.text

time.sleep(3)

driver.quit()