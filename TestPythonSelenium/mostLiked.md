# Explicação do Código `mostLiked.py`

O arquivo `mostLiked.py` contém um teste de integração que acessa o módulo **Buzz** do sistema OrangeHRM e clica no botão **"Most Liked Posts"** (Postagens Mais Curtidas). Ele depende do arquivo `login.py` para realizar a autenticação antes de executar as ações.

#### O que eu fiz?

- Criei um teste que reaproveita a função `test_login()` do `login.py` para iniciar a automação já logado na home.
- Após o login, o script acessa o menu Buzz.
- Em seguida, espera o botão **"Most Liked Posts"** aparecer e clica nele.
- O teste usa `WebDriverWait` para evitar erros de carregamento da página.
- O driver é retornado ao final da função para permitir que outros testes possam dar continuidade, se necessário.

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
# O arquivo deve incluir Selenium e outras libs utilizadas no projeto
```

### Como executar o `mostLiked.py`

```bash
python mostLiked.py
```

## Código:

- O teste inicia com login automatizado (mock de usuário admin).
- Em seguida, acessa o menu Buzz via XPath.
- Usa `WebDriverWait` com `expected_conditions` para aguardar o botão **Most Liked Posts**.
- Realiza o clique e mostra em ordem descresente qual Post tem mais curtidads.
- Encerra o navegador ao fim do teste.

```python
def mostLiked():
  driver = test_login("Admin", "admin123")
  driver.implicitly_wait(5)
  driver.find_element(By.XPATH, "//a[@href='/web/index.php/buzz/viewBuzz']").click()

  time.sleep(5)
  wait = WebDriverWait(driver, 10)
  #Pega os botões e clica no "Most Liked Posts"
  most_liked = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Most Liked Posts')]")))
  most_liked.click()

  time.sleep(3)

  return driver
```

### Tratamento de erros

O script está preparado para lidar com erros de timeout ou elementos não encontrados:

```python
except TimeoutException:
    print("Login test failed: Timeout while waiting for elements.")
except NoSuchElementException as e:
    print(f"Login test failed: Element not found - {e}")
```

---

**Qualquer dúvida, fico à disposição!**