import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains  # Importación correcta de ActionChains


# Configura las opciones de Chrome
options = Options()
# options.add_argument('--headless')  # Comenta o elimina esta línea para ver la interfaz gráfica del navegador
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

print("Opciones de Chrome configuradas.")

# Inicializa el driver de Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
print("Driver de Chrome inicializado.")

# Configura el tiempo máximo de espera
wait = WebDriverWait(driver, 10)

# Abre la página de inicio de sesión
print("Abriendo la página de inicio de sesión...")
driver.get('https://nasini.aunesa.com/Irmo/')

try:
    # Realiza el proceso de inicio de sesión
    print("Rellenando el formulario de inicio de sesión...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'gwt-uid-')]"))).send_keys('edalessandro')
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'gwt-uid-')][@type='password']"))).send_keys('123456-nasini')
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-button v-widget v-has-width']"))).click()
    print("Formulario de inicio de sesión enviado.")

    # Verifica si el inicio de sesión fue exitoso
    print("Verificando el inicio de sesión exitoso...")
    elemento_especifico = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "elemento_especifico_css")))
    print("Inicio de sesión exitoso. Captura de pantalla guardada.")
    driver.save_screenshot('inicio_sesion_exitoso.png')
except Exception as e:
    print(f"Error o inicio de sesión fallido: {e}")
    driver.save_screenshot('error_o_fallo_inicio_sesion.png')

    # Uso de ActionChains para realizar acciones complejas
    actions = ActionChains(driver)

    # Definiciones de XPaths para el menú rápido
    print("Interactuando con el menú rápido...")
    MENU_RAPIDO_INPUT_XPATH = '//*[@id="Irmo-2287787"]/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[5]/div/input'
    MENU_RAPIDO_SELECT_XPATH = '//*[@id="VAADIN_COMBOBOX_OPTIONLIST"]/div/div[2]/table/tbody/tr/td/span'
    consulta = 'Administración de especies :: Unidades'

    # Espera y escribe en el menú rápido
    wait.until(EC.presence_of_element_located((By.XPATH, MENU_RAPIDO_INPUT_XPATH)))
    driver.find_element(By.XPATH, MENU_RAPIDO_INPUT_XPATH).send_keys(consulta)
    print('Consulta enviada, esperando a las opciones...')

    time.sleep(5)  # Espera para que las opciones aparezcan

    # Selecciona la opción en el menú rápido
    wait.until(EC.presence_of_element_located((By.XPATH, MENU_RAPIDO_SELECT_XPATH)))
    driver.find_element(By.XPATH, MENU_RAPIDO_SELECT_XPATH).click()
    print("Opción seleccionada en el menú rápido.")

    # Escribir en el campo de input
    input_field = driver.find_element(By.CSS_SELECTOR, "input.v-filterselect-input")
    input_field.send_keys("1")

    # Esperar a que el botón sea clickeable y hacer clic (si es necesario)
    time.sleep(2)  # Ajusta según sea necesario para tu página
    first_button = driver.find_element(By.CSS_SELECTOR, "div.v-button")
    first_button.click()

    # Esperar a que el botón "Buscar" sea clickeable y hacer clic
    time.sleep(2)  # Ajusta según sea necesario para tu página
    buscar_button = driver.find_element(By.XPATH, "//span[contains(@class, 'v-button-caption') and text()='Buscar']")
    buscar_button.click()

   # Localiza el elemento en el que deseas hacer clic derecho
    element_to_right_click = driver.find_element(By.TAG_NAME, 'body')

    # Inicializa ActionChains
    actions = ActionChains(driver)

    # Realiza clic derecho en el elemento especificado
    actions.context_click(element_to_right_click).perform()

    # Ahora, necesitas seleccionar la opción "Exportar como XLSX" del menú contextual
    # Esto puede ser desafiante porque el menú contextual es generado dinámicamente y podría no estar presente en el DOM hasta que se realice el clic derecho
    # Localiza el elemento por su texto o alguna otra propiedad única
    export_option = driver.find_element(By.XPATH, "//td[contains(@class, 'gwt-MenuItem') and contains(., 'Exportar como XLSX')]")

    # Haz clic en la opción de exportar
    export_option.click()


    # Pausa para inspección manual
    input("Presiona Enter en la consola para continuar después de la inspección...")


#except Exception as e:
   #print(f"Error durante la ejecución: {e}")
   # driver.save_screenshot('error_during_execution.png')
#finally:
    # Cierra el navegador después de la ejecución
   # print("Cerrando el navegador...")
   # driver.quit()
