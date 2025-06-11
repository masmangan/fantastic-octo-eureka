# Explicação do Código `time_at_work` 

O arquivo `time_at_work.py` contém o código para entrada da data, horário e descrição de entrada no trabalho, e o de saída.

## Setup para o teste

### Criar e ativar um ambiente virtual - venv

```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
# .\venv\Scripts\activate  # No Windows
```

### Como instalar dependências

Certifique-se de estar na pasta **TestPythonSelenium**

```bash
pip install -r requirements.txt
# deve conter todos as lib do projeto, conforme o uso
```

### Como executar o `time_at_work`

```bash
python Tests/time_at_work.py
```

## Código:

- Utilizei o código do `login.py` para autenticação
- Na página de dashboard, cliquei no botão do card de Punch In/ Punch Out
- Na aba de Punch In, inseri uma descrição na textarea de `Note`
- Confirmei no botão `In`
- Na aba de Punch Out, alterei o horário de saída e coloquei uma descrição de saída
- Confirmei no botão `Out`

```python
def time_at_work(noteIn, noteOut):
    driver = test_login("Admin", "admin123")
    
    driver.find_element(By.CSS_SELECTOR, ".oxd-icon-button.oxd-icon-button--solid-main.orangehrm-attendance-card-action").click()
    time.sleep(5)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-icon.bi-clock.oxd-time-input--clock'))).click()

    textarea_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-textarea.oxd-textarea--active.oxd-textarea--resize-vertical'))
    )
    textarea_field.clear()
    textarea_field.send_keys(noteIn)

    driver.find_element(By.CSS_SELECTOR, '.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space').click()
    print("Time in recorded successfully.")
    time.sleep(10)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-icon.bi-clock.oxd-time-input--clock'))).click()

    for i in range(3):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.oxd-icon.bi-chevron-down.oxd-icon-button__icon.oxd-time-hour-input-down'))
        ).click()

    textarea_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-textarea.oxd-textarea--active.oxd-textarea--resize-vertical'))
    )
    textarea_field.clear()
    textarea_field.send_keys(noteOut)

    driver.find_element(By.CSS_SELECTOR, '.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space').click()
    print("Time out recorded successfully.")

    time.sleep(10)

    return driver
```