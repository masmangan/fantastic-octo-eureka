# test_view_employee_profile.py

from login import test_login  # Importa a função de login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_view_employee_profile(driver):
    try:
        # Localizando o link "PIM" pelo href e clicando nele
        pim_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/web/index.php/pim/viewPimModule"]'))
        )
        pim_menu.click()

        # Localizando o campo de busca pelo placeholder "Type for hints..."
        search_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))
        )
        search_field.send_keys("John Doe")

        # Localizando o botão "Search" e clicando nele
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary"))
        )
        search_button.click()

        # Esperar o resultado da busca
        time.sleep(3)

        # Verificar se o nome "John Doe" existe na lista de empregados
        employee_row = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'John')]/ancestor::div[contains(@class, 'oxd-table-row')]"))
        )

        # Asserção para garantir que o nome foi encontrado
        assert "John" in employee_row.text and "Doe" in employee_row.text

        # Clica na linha para abrir o perfil
        employee_row.click()

        # Esperar um pouco para garantir que o perfil foi aberto
        time.sleep(5)
        
        # Busca pela mensagem de sucesso após abrir o perfil
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h6.oxd-text.oxd-text--h6.--strong"))
        )

        # Agora que o elemento foi encontrado realiza a asserção
        assert "John Doe" in success_message.text

    except Exception as e:
        print(f"Falha ao abrir o perfil do funcionário: {e}")

if __name__ == "__main__":
    try:
        driver = test_login("Admin", "admin123")  # Realiza o login
        test_view_employee_profile(driver)  # Executa o teste para abrir o perfil do funcionário
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()  # Fecha o navegador no final
