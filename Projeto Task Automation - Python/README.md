# Automação de Cadastro de Produtos com Python

## Descrição
Este projeto tem como objetivo automatizar o processo de cadastro de produtos em um sistema online. Utilizando Python, o script acessa uma plataforma específica, faz o login, importa uma base de dados e cadastra os produtos de forma automática até que todos os produtos sejam inseridos.

## Passos da Automação

1. **Entrar no site**: O script acessa o link da plataforma:
   - [Plataforma de Cadastro](https://dlp.hashtagtreinamentos.com/python/intensivao/login)
   
2. **Fazer Login**: Utilizando as credenciais fornecidas, o login é realizado de forma automatizada.

3. **Importar Base de Dados**: O script carrega a base de dados (por exemplo, um arquivo Excel ou CSV) contendo os produtos a serem cadastrados.

4. **Cadastrar 1 Produto**: A automação faz o cadastro do primeiro produto da lista.

5. **Repetir o Processo**: O processo de cadastro é repetido até que todos os produtos da base de dados tenham sido inseridos no sistema.

## Requisitos

Python  

Bibliotecas:
pandas
pyautogui
