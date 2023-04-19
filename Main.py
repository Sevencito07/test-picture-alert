from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from PIL import ImageGrab
import time

# Iniciar el navegador web en modo headless
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Navegar a la página web deseada
driver.get('https://ejemplo.com')

while True:
    # Esperar a que aparezca una alerta
    alert = Alert(driver)
    alert_text = alert.text
    while not alert_text:
        alert_text = alert.text

    # Tomar una captura de pantalla de la pantalla actual
    screenshot = ImageGrab.grab()

    # Guardar la captura de pantalla en un archivo
    screenshot.save('captura.png')

    # Esperar 10 segundos antes de buscar otra alerta
    time.sleep(10)
