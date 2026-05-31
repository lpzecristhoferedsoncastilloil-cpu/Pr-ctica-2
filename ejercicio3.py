
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://automationexercise.com")

driver.maximize_window()

time.sleep(3)

products_link = driver.find_element(By.XPATH, '//a[contains(text(), "Products")]')
products_link.click()
time.sleep(3)

search_input = driver.find_element(By.XPATH, '//input[contains(@id, "search_product")]')
search_input.click()
search_input.send_keys("shirt")

time.sleep(3)

search_button = driver.find_element(By.XPATH, '//button[contains(@id, "submit_search") or contains(text(), "Search")]')
search_button.click()

time.sleep(3)

result_heading = driver.find_element(By.XPATH, '//h2[contains(translate(normalize-space(.), "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "SEARCHED PRODUCTS")]')
print("Resultado encontrado:", result_heading.text)
assert "SEARCHED PRODUCTS" in result_heading.text.upper()

products = driver.find_elements(By.XPATH, '//div[contains(@class, "product-overlay")] | //div[contains(@class, "product")]//h2')
print("Cantidad de resultados encontrados:", len(products))
assert len(products) > 0

time.sleep(3)

driver.quit()