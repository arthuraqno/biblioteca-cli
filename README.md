# 🏛️ Biblioteca CLI

Sistema de gerenciamento de biblioteca no terminal, desenvolvido em Python.

## 📋 Funcionalidades

- Cadastrar livros e usuários
- Realizar e devolver empréstimos
- Bloqueio automático de usuários em atraso
- Dados persistidos em banco de dados PostgreSQL

## 📁 Estrutura do Projeto

biblioteca-cli/
├── main.py
├── base.py
├── database.py
├── models/
│ ├── livro.py
│ ├── usuario.py
│ └── emprestimo.py
└── services/
└── biblioteca.py


## ▶️ Como rodar

1. Crie um banco de dados PostgreSQL chamado `biblioteca_db`
2. Configure a conexão em `database.py` com seu usuário e senha
3. Execute `python database.py` para criar as tabelas
4. Execute `python main.py` para iniciar o sistema

## 🛠️ Tecnologias

- Python 3.14
- PostgreSQL
- SQLAlchemy (ORM)
- psycopg2

## 📚 Aprendizados

- Orientação a objetos, herança e relacionamentos entre tabelas
- Mapeamento objeto-relacional (ORM) com SQLAlchemy
- Chaves estrangeiras e relacionamentos (Foreign Key, relationship)
- Banco de dados relacional com PostgreSQL
- Menus interativos no terminal