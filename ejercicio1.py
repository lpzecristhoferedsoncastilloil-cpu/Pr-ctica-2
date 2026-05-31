from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.maximize_window()

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.click()
user_name.send_keys("standard_user")

time.sleep(5)

password = driver.find_element(By.ID, 'password')
password.click()
password.send_keys("secret_sauce")

boton_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
boton_login.click()
time.sleep(5)

driver.quit()