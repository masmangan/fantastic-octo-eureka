# Explicação do Código `new_post` 

O arquivo `new_post.py` contém o código que serve para o processo de criação de um novo post.

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

### Como executar o `new_post`

```bash
python Tests/new_post.py
```

## Código:

- Utilizei o código do `login.py` para autenticação
- Na aba lateral, cliquei no botão que nos redireciona para `/web/index.php/buzz/viewBuzz`
- No input de descrição do post, inseri um input já pré-programado
- Cliquei no botão de `Post` para enviar publicação
- Dei refresh na página para visualizar o meu post

```python
def new_post(content):
    driver = test_login("Admin", "admin123")

    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@href='/web/index.php/buzz/viewBuzz']").click()

    textarea_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-buzz-post-input'))
    )
    textarea_field.clear()
    textarea_field.send_keys(content)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, '.oxd-button.oxd-button--medium.oxd-button--main').click()

    driver.refresh()
    time.sleep(10)
    return driver
```