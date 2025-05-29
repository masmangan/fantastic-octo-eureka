# Explicação do Código `login.py` 

O arquivo `login.py` contém o código que serve para o processo de autenticação de usuários. Ele pode incluir funções para solicitar usuário e senha, validar credenciais e exibir mensagens de sucesso ou erro.

#### O que eu fiz?

- Fiz um fork desse repositório, está disponivel no meu github!
- Usei a lib do selenium para abrir o projeto no link do servidor de testes.
- Caso o processo não seja concluído, ele deve retornar erro
- Creio que vários colegas podem usar esse método, para ja obterem um teste que inicie na "home"
- Por conta do item acima, fiz esse método retornar o driver. Para prosseguir as atividades.

## Setup para o teste

### Criar e ativar um ambiente virtual - venv

```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
# .\venv\Scripts\activate  # No Windows
```

### Como instalar dependências 

```bash
pip install -r requirements.txt
# deve conter todos as lib do projeto, conforme o uso
```

### Como executar o `login.py`

```bash
python login.py
```

## Código:

- Mockei os dados de admin para testes, como explicado no pdf do trabalho
- Procurei os inputs de nome e senha
- Procurei e cliquei no botão selecionado 

```python
def test_login(username, password):

  driver = webdriver.Chrome()
  driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
  driver.maximize_window()
  input_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Username"]')))
  input_field.clear()
  input_field.send_keys(username)
  input_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Password"]')))
  input_field.clear()
  input_field.send_keys(password)
  driver.find_element(By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button').click()
  time.sleep(20)
  driver.implicitly_wait(20)
```

**Qualquer dúvida, eu fico a disposição!**