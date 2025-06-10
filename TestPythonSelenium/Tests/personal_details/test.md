# Teste Automatizado: Personal Details (OrangeHRM)

Este teste automatizado valida o preenchimento e envio do formulário "Personal Details" no OrangeHRM.

## Objetivo
Garantir que o formulário de dados pessoais do funcionário aceita, valida e salva corretamente as informações, incluindo campos obrigatórios, dropdowns, datas e seleção de gênero.

## Pré-requisitos
- Python 3 instalado
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome (no PATH)
- Instalar dependências:
  ```bash
  pip install -r ../../requirements.txt
  ```

## Como rodar o teste
Execute na pasta `personal_details`:
```bash
python test_personal_details.py
```
Ou, se preferir, com pytest:
```bash
pytest test_personal_details.py -s
```

## O que o teste faz
- Realiza login no OrangeHRM demo
- Acessa o menu "My Info" > "Personal Details"
- Limpa todos os campos do formulário
- Preenche:
  - Nome completo (First, Middle, Last)
  - Employee Id (menos de 10 caracteres)
  - Other Id
  - Driver's License Number
  - License Expiry Date (yyyy-dd-mm)
  - Nationality (dropdown)
  - Marital Status (dropdown)
  - Date of Birth (yyyy-dd-mm)
  - Gender (radio)
- Valida que o botão Save está habilitado
- Salva e verifica mensagem de sucesso
