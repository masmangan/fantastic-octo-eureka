# test_add_driver_license.py

from employeeList import test_view_employee_profile
from login import test_login  # Importa a função de login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_add_middle_name(driver):
    try:
        
        # Localizar o campo para o nome do meio
        middle_name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='middleName']"))
        )

        # Limpar o campo antes de digitar
        middle_name_input.clear()

        # Preencher o campo com um nome do meio
        middle_name_input.send_keys("Silva")

        # Salvar as alterações
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        save_button.click()

        # Esperar um pouco para garantir que as alterações foram salvas
        time.sleep(10)

        # Busca pela mensagem de sucesso após adicionar o nome do meio
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h6.oxd-text.oxd-text--h6.--strong"))
        )

        # Agora que o elemento foi encontrado realiza a asserção
        assert "John Doe" in success_message.text
        print("Funcionário modificado com sucesso!")

    except Exception as e:
        print(f"Falha ao adicionar nome do meio: {e}")

if __name__ == "__main__":
    try:
        driver = test_view_employee_profile( test_login("Admin", "admin123") ) # Realiza o login e abre o perfil do empregado
        test_add_middle_name(driver)
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()  # Fecha o navegador no final
