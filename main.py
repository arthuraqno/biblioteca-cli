from models.livro import Livro
from models.usuario import Usuario
from services.biblioteca import Biblioteca

biblioteca = Biblioteca()
biblioteca.carregar_dados()
biblioteca.verificar_atrasos()

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
            isbn = int(input("ISBN: "))
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            livro = Livro(isbn, titulo, autor, ano)
            biblioteca.cadastrar_livro(livro)

        elif opcao == "2":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            usuario = Usuario(nome, telefone)
            biblioteca.cadastrar_usuario(usuario)

        elif opcao == "3":
            titulo = input("Título do livro: ")
            nome = input("Nome do usuário: ")
            livro = biblioteca.buscar_livro(titulo)
            usuario = biblioteca.buscar_usuario(nome)
            if livro is None:
                print("Livro não encontrado.")
            elif usuario is None:
                print("Usuário não encontrado.")
            else:
                biblioteca.emprestar_livro(livro, usuario)

        elif opcao == "4":
            titulo = input("Título do livro: ")
            nome = input("Nome do usuário: ")
            livro = biblioteca.buscar_livro(titulo)
            usuario = biblioteca.buscar_usuario(nome)
            if livro is None:
                print("Livro não encontrado.")
            elif usuario is None:
                print("Usuário não encontrado.")
            else:
                biblioteca.devolver_livro(livro, usuario)

        elif opcao == "5":
            biblioteca.listar_livros()

        elif opcao == "6":
            biblioteca.listar_usuarios()

        elif opcao == "7":
            biblioteca.salvar_dados()
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida.")

menu()
