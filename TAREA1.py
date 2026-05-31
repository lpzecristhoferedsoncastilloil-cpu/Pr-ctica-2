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

# 2. Hacer clic en el menú 'Signup / Login' usando XPATH
signup_login_link = driver.find_element(By.XPATH, '//a[contains(@href, "/login")]')
driver.execute_script("arguments[0].click();", signup_login_link)
time.sleep(3)

# Eliminar anuncios en la página de registro/login
driver.execute_script("document.querySelectorAll('iframe, ins, .adsbygoogle').forEach(el => el.remove());")

# 3. Llenar el formulario de Registro (Nombre y Correo) usando NAME y CSS SELECTOR
name_input = driver.find_element(By.NAME, "name")
driver.execute_script("arguments[0].click();", name_input)
name_input.send_keys("Tester Automatizado")
time.sleep(2)

# Generar un correo dinámico usando el timestamp para que se pueda ejecutar repetidas veces sin error de correo ya existente
email_dinamico = f"tester_qa_{int(time.time())}@gmail.com"
email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
driver.execute_script("arguments[0].click();", email_input)
email_input.send_keys(email_dinamico)
time.sleep(2)



# 4. Hacer clic en el botón 'Signup' usando XPATH
signup_button = driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]')
driver.execute_script("arguments[0].click();", signup_button)
time.sleep(3)

# Eliminar anuncios en la página de registro detallado
driver.execute_script("document.querySelectorAll('iframe, ins, .adsbygoogle').forEach(el => el.remove());")

# 5. Completar los campos obligatorios del registro detallado usando ID y NAME
# Seleccionar género (Mr.)
gender_radio = driver.find_element(By.ID, "id_gender1")
driver.execute_script("arguments[0].click();", gender_radio)

# Contraseña
password_input = driver.find_element(By.ID, "password")
driver.execute_script("arguments[0].click();", password_input)
password_input.send_keys("Password123!")

# Datos de dirección (Campos requeridos)
first_name = driver.find_element(By.ID, "first_name")
first_name.send_keys("Tester")

last_name = driver.find_element(By.ID, "last_name")
last_name.send_keys("Automatizado")

address = driver.find_element(By.ID, "address1")
address.send_keys("Calle Falsa 123")

state = driver.find_element(By.ID, "state")
state.send_keys("Lima")

city = driver.find_element(By.ID, "city")
city.send_keys("Miraflores")

zipcode = driver.find_element(By.ID, "zipcode")
zipcode.send_keys("15046")

mobile_number = driver.find_element(By.ID, "mobile_number")
mobile_number.send_keys("999999999")
time.sleep(2)

# 6. Hacer clic en el botón 'Create Account' usando XPATH
create_account_button = driver.find_element(By.XPATH, '//button[@data-qa="create-account"]')
driver.execute_script("arguments[0].click();", create_account_button)
time.sleep(3)

# --- VALIDACIONES (Asserts) y EVIDENCIAS ---

# Elemento del título de confirmación
success_heading = driver.find_element(By.XPATH, '//h2[@data-qa="account-created"]')
print("Texto encontrado en pantalla:", success_heading.text)

# Assert 1: Validar que el texto en pantalla sea el correcto (Cuenta Creada)
assert "ACCOUNT CREATED!" in success_heading.text.upper()

# Assert 2: Validar que el botón 'Continue' de éxito esté presente en la página
continue_button = driver.find_element(By.XPATH, '//a[@data-qa="continue-button"]')
assert continue_button.is_displayed()

# Evidencia: Guardar la captura de pantalla requerida
driver.save_screenshot("evidencia_ejercicio1_registro.png")
print("Captura de pantalla guardada exitosamente.")

time.sleep(3)

# Cerrar el navegador
driver.quit()