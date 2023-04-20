# Cargar la biblioteca Selenium.WebDriver
Add-Type -Path "C:\path\to\Selenium.WebDriver.dll"

# Configurar el navegador Chrome
$options = New-Object OpenQA.Selenium.Chrome.ChromeOptions
$options.AddArgument("--headless")
$driver = New-Object OpenQA.Selenium.Chrome.ChromeDriver($options)

# Navegar a la página web deseada
$driver.Navigate().GoToUrl("https://ejemplo.com")

while($true) {
    # Esperar a que aparezca una alerta
    $alert = $driver.SwitchTo().Alert()
    $alertText = $alert.Text
    while(!$alertText) {
        $alertText = $alert.Text
    }

    # Tomar una captura de pantalla de la pantalla actual
    $screenshot = $driver.GetScreenshot()

    # Guardar la captura de pantalla en un archivo
    $screenshot.SaveAsFile("captura.png", "png")

    # Esperar 10 segundos antes de buscar otra alerta
    Start-Sleep -Seconds 10
}
