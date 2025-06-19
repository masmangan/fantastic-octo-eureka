# test_add_employee.py

from login import test_login  # Importa a função de login
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_add_employee(driver):
    try:
        # Localizando o link "PIM" pelo href e clicando nele
        pim_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/web/index.php/pim/viewPimModule"]'))
        )
        pim_menu.click()

        # Clicar no link "Add Employee" para adicionar um novo funcionário
        add_employee_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Add Employee']"))
        )
        add_employee_button.click()

        # Preencher os campos do formulário de cadastro de funcionário
        first_name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='firstName']"))
        )
        first_name_field.send_keys("John")

        last_name_field = driver.find_element(By.XPATH, "//input[@name='lastName']")
        last_name_field.send_keys("Doe")

        # Clicar no botão "Save" para salvar o novo funcionário
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        save_button.click()

        # Esperar um pouco para garantir que o funcionário foi adicionado
        time.sleep(10)

        # Busca pela mensagem de sucesso após adicionar o funcionário
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h6.oxd-text.oxd-text--h6.--strong"))
        )

        # Agora que o elemento foi encontrado realiza a asserção
        assert "John Doe" in success_message.text
        print("Funcionário adicionado com sucesso!")
        
    except Exception as e:
        print(f"Falha ao adicionar funcionário: {e}")

if __name__ == "__main__":
    try:
        driver = test_login("Admin", "admin123")  # Realiza o login
        test_add_employee(driver)  # Executa o teste para adicionar o funcionário
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
