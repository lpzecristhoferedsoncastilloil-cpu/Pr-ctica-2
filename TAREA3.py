from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Inicializar el navegador y abrir la página
driver = webdriver.Chrome()
driver.get("https://automationexercise.com")
driver.maximize_window()
time.sleep(3)

# Eliminar anuncios iniciales
driver.execute_script("document.querySelectorAll('iframe, ins, .adsbygoogle').forEach(el => el.remove());")

# 2. Validar presencia del encabezado usando ID (cumple con requisito de localizador ID) y navegar
header = driver.find_element(By.ID, "header")
assert header.is_displayed()

login_menu = driver.find_element(By.XPATH, '//a[contains(@href, "/login")]')
driver.execute_script("arguments[0].click();", login_menu)
time.sleep(3)

# Eliminar anuncios en la página de login
driver.execute_script("document.querySelectorAll('iframe, ins, .adsbygoogle').forEach(el => el.remove());")

# 3. Introducir datos incorrectos usando CSS SELECTOR y NAME
email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-email"]')
driver.execute_script("arguments[0].click();", email_input)
email_input.send_keys("error@gmail.com")
time.sleep(2)

password_input = driver.find_element(By.NAME, "password")
driver.execute_script("arguments[0].click();", password_input)
password_input.send_keys("error")
time.sleep(2)

# 4. Hacer clic en el botón de Login usando CSS SELECTOR
login_button = driver.find_element(By.CSS_SELECTOR, 'button[data-qa="login-button"]')
driver.execute_script("arguments[0].click();", login_button)
time.sleep(4)

# Eliminar anuncios antes de validar
driver.execute_script("document.querySelectorAll('iframe, ins, .adsbygoogle').forEach(el => el.remove());")

# --- VALIDACIONES (Asserts) y EVIDENCIAS ---

# Localizar el mensaje de error en pantalla usando XPATH
error_message = driver.find_element(By.XPATH, '//p[contains(text(), "incorrect")]')
print("Mensaje de error detectado:", error_message.text)

# Assert 1: Validar que el mensaje de error esté visible
assert error_message.is_displayed()

# Assert 2: Validar el texto exacto del mensaje de error del sistema
assert "Your email or password is incorrect!" in error_message.text

# Evidencia: Guardar captura de pantalla
driver.save_screenshot("evidencia_tarea3_login_incorrecto.png")
print("Captura de pantalla de Tarea 3 guardada.")

time.sleep(3)
driver.quit()