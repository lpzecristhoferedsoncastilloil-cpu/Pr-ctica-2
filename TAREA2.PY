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

# 3. Introducir correo y contraseña válidos usando CSS SELECTOR y NAME
# Usar el correo y la contraseña de la Tarea 1 para loguear correctamente
email_valido = "correo_prueba_2026_99@gmail.com"
password_valido = "Password123!"

email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-email"]')
driver.execute_script("arguments[0].click();", email_input)
email_input.send_keys(email_valido)
time.sleep(2)

password_input = driver.find_element(By.NAME, "password")
driver.execute_script("arguments[0].click();", password_input)
password_input.send_keys(password_valido)
time.sleep(2)

# 4. Hacer clic en el botón de Login usando CSS SELECTOR
login_button = driver.find_element(By.CSS_SELECTOR, 'button[data-qa="login-button"]')
driver.execute_script("arguments[0].click();", login_button)
time.sleep(4)

# Eliminar anuncios después del login
driver.execute_script("document.querySelectorAll('iframe, ins, .adsbygoogle').forEach(el => el.remove());")

# --- VALIDACIONES (Asserts) y EVIDENCIAS ---

# Buscar el botón de Logout y el texto de usuario logueado usando XPATH
logout_btn = driver.find_element(By.XPATH, '//a[contains(@href, "/logout")]')
user_status_text = driver.find_element(By.XPATH, '//i[@class="fa fa-user"]/parent::a').text
print("Texto de usuario activo:", user_status_text)

# Assert 1: Validar que el botón 'Logout' esté visible en el menú
assert logout_btn.is_displayed()

# Assert 2: Validar que aparezca el mensaje de que iniciaste sesión
assert "Logged in as" in user_status_text

# Evidencia: Guardar captura de pantalla al final de la sesión exitosa
driver.save_screenshot("evidencia_tarea2_login_correcto.png")
print("Captura de pantalla de Tarea 2 guardada.")

time.sleep(3)
driver.quit()