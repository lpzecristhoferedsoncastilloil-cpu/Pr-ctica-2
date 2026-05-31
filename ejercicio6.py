
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/alerts")

driver.execute_script("window.scrollBy(0, 500)")

driver.find_element(By.ID, "alertButton").click()

alert = Alert(driver)   

print(alert.text)

alert.accept()

time.sleep(5)
driver.quit()