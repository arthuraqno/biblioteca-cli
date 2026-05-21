# 🏛️ Biblioteca CLI

Sistema de gerenciamento de biblioteca no terminal, desenvolvido em Python.

## 📋 Funcionalidades

- Cadastrar livros e usuários
- Realizar e devolver empréstimos
- Bloqueio automático de usuários em atraso
- Dados persistidos em JSON

## 📁 Estrutura do Projeto
biblioteca-cli/
├── main.py
├── models/
│   ├── livro.py
│   ├── usuario.py
│   └── emprestimo.py
├── services/
│   └── biblioteca.py
└── data/
├── livros.json
├── usuarios.json
└── emprestimos.json

## ▶️ Como rodar

```bash
cd biblioteca-cli
python main.py
```

## 🛠️ Tecnologias

- Python 3.14
- JSON para persistência de dados

## 📚 Aprendizados

- Orientação a objetos (classes, encapsulamento)
- Separação de responsabilidades
- Persistência de dados com JSON
- Menus interativos no terminal