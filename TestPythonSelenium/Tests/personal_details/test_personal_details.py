from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.keys import Keys

# Função utilitária para login (reutiliza o padrão do login.py)
def login(driver, username, password):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Username"]'))
    ).send_keys(username)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Password"]'))
    ).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button').click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//span[text()="My Info"]'))
    )

def acessar_my_info(driver):
    # Clica no menu lateral "My Info"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="My Info"]'))
    ).click()
    # Aguarda a aba "Personal Details" estar visível
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//h6[text()="Personal Details"]'))
    )

def limpar_todos_inputs(driver):
    # Limpa todos os campos de input de texto visíveis
    inputs = driver.find_elements(By.XPATH, '//input[@class="oxd-input oxd-input--active"]')
    for campo in inputs:
        try:
            campo.clear()
        except Exception:
            pass

def limpar_input_totalmente(elemento):
    try:
        elemento.send_keys(Keys.CONTROL, 'a')
        elemento.send_keys(Keys.BACKSPACE)
    except Exception:
        pass

def limpar_input_data(driver, xpath):
    campo = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].removeAttribute('readonly')", campo)
    campo.send_keys(Keys.CONTROL, 'a')
    campo.send_keys(Keys.BACKSPACE)
    return campo

def preencher_formulario(driver, dados):
    limpar_todos_inputs(driver)
    # 1. First Name
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'firstName'))).clear()
    driver.find_element(By.NAME, 'firstName').send_keys(dados['firstName'])
    # 2. Middle Name
    driver.find_element(By.NAME, 'middleName').clear()
    driver.find_element(By.NAME, 'middleName').send_keys(dados['middleName'])
    # 3. Last Name
    driver.find_element(By.NAME, 'lastName').clear()
    driver.find_element(By.NAME, 'lastName').send_keys(dados['lastName'])
    # 4. Employee Id
    campo_employee_id = driver.find_element(By.XPATH, '//label[text()="Employee Id"]/../following-sibling::div/input')
    limpar_input_totalmente(campo_employee_id)
    campo_employee_id.send_keys(dados['employeeId'])
    # 5. Other Id
    driver.find_element(By.XPATH, '//label[text()="Other Id"]/../following-sibling::div/input').clear()
    driver.find_element(By.XPATH, '//label[text()="Other Id"]/../following-sibling::div/input').send_keys(dados['otherId'])
    # 6. Driver's License Number
    driver.find_element(By.XPATH, '//label[text()="Driver\'s License Number"]/../following-sibling::div/input').clear()
    driver.find_element(By.XPATH, '//label[text()="Driver\'s License Number"]/../following-sibling::div/input').send_keys(dados['licenseNumber'])
    # 7. License Expiry Date
    input_expiry = limpar_input_data(driver, '//label[contains(text(),"License Expiry Date")]/../following-sibling::div//input')
    input_expiry.send_keys(dados['licenseExpiry'])
    # 8. Nationality (dropdown)
    driver.find_element(By.XPATH, '//label[text()="Nationality"]/../following-sibling::div//div[contains(@class,"oxd-select-text")]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, f'//div[@role="option"]/span[text()="{dados["nationality"]}"]').click()
    # 9. Marital Status (dropdown)
    driver.find_element(By.XPATH, '//label[text()="Marital Status"]/../following-sibling::div//div[contains(@class,"oxd-select-text")]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, f'//div[@role="option"]/span[text()="{dados["maritalStatus"]}"]').click()
    # 10. Date of Birth
    input_birth = limpar_input_data(driver, '//input[@placeholder="yyyy-dd-mm"]')
    input_birth.send_keys(dados['dob'])
    # 11. Gender
    if dados['gender'].lower() == 'male':
        driver.find_element(By.XPATH, '//input[@type="radio" and @value="1"]/following-sibling::span').click()
    else:
        driver.find_element(By.XPATH, '//input[@type="radio" and @value="2"]/following-sibling::span').click()

def test_adicao_dados_pessoais():
    driver = webdriver.Chrome()
    try:
        login(driver, "Admin", "admin123")
        acessar_my_info(driver)
        dados = {
            'firstName': 'João',
            'middleName': 'da Silva',
            'lastName': 'Teste',
            'employeeId': '123456789',
            'otherId': '54321',
            'licenseNumber': 'A1234567',
            'licenseExpiry': '2030-31-12',
            'nationality': 'American',
            'maritalStatus': 'Single',
            'dob': '1990-20-10',
            'gender': 'Male'
        }
        preencher_formulario(driver, dados)
        # Verifica se o botão Save está habilitado
        save_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        assert save_button.is_enabled(), "Botão Save deve estar habilitado com campos válidos."
        save_button.click()
        # Espera mensagem de sucesso
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Success")]'))
        )
        print("Teste de adição de dados pessoais passou.")
    except Exception as e:
        print(f"Falha no teste de adição de dados pessoais: {e}")
        raise
    finally:
        driver.quit()

if __name__ == "__main__":
    test_adicao_dados_pessoais() 