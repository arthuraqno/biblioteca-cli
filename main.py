from models.livro import Livro
from models.usuario import Usuario
from services.biblioteca import Biblioteca

biblioteca = Biblioteca()

def menu():
    while True:
        print("\n=====================================")
        print("       🏛️  BIBLIOTECA CLI")
        print("=====================================")
        print("1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Listar livros")
        print("6. Listar usuários")
        print("7. Sair")
        print("=====================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano_publicacao = int(input("Ano: "))
            biblioteca.cadastrar_livros(titulo, autor, ano_publicacao, disponivel=True)
        elif opcao == "2":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            matricula = int(input("Matricula: "))
            biblioteca.cadastrar_usuarios(nome, telefone, matricula, em_atraso=False)
        elif opcao == "3":
            titulo = input("Título do livro: ")
            nome = input("Nome do usuário: ")
            biblioteca.emprestar_livro(titulo, nome)
        elif opcao == "4":
            titulo = input("Título do livro: ")
            nome = input("Nome do usuário: ")
            biblioteca.devolver_livro(titulo, nome)

        elif opcao == "5":
            biblioteca.listar_livros()

        elif opcao == "6":
            biblioteca.listar_usuarios()

        elif opcao == "7":
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida.")

menu()
