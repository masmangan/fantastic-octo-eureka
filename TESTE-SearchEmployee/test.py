from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

CHROME_DRIVER_PATH = './chromedriver-mac-arm64/chromedriver'

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)  
try:
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()

    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))).click()

    search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
    search_input.send_keys("Ranga")
    time.sleep(1)
    search_input.send_keys(Keys.ARROW_DOWN)
    search_input.send_keys(Keys.ENTER)

    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    search_button.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-body']")))

    time.sleep(1) 
    table_cells = driver.find_elements(By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell']")

    print("\n📋 Conteúdo da tabela:")
    for cell in table_cells:
        try:
            print(cell.text)
        except:
            print("[Erro ao acessar célula]")

    found = any("Ranga" in cell.text for cell in table_cells)
    assert found, "O nome 'Ranga' não foi encontrado na tabela."
    print("✅ TESTE PASSOU: Funcionária 'Ranga' encontrada na tabela.")

except Exception as e:
    print("❌ TESTE FALHOU:")
    traceback.print_exc()

finally:
    driver.quit()