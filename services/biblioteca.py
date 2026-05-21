import json
from models.livro import Livro
from models.usuario import Usuario
from models.emprestimo import Emprestimo
from datetime import date

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    #--------- Livros ---------

    def cadastrar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro disponível na biblioteca.")
            return
        for livro in self.livros:
            print(livro)


    #--------- Usuários ---------

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuário '{usuario.nome}' cadastrado com sucesso.")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        for usuario in self.usuarios:
            print(usuario)

    #--------- Empréstimos ---------

    def emprestar_livro(self, livro, usuario):
        if not livro.disponivel:
            print(f"Livro '{livro.titulo}' não está disponível.")
            return
        if usuario.em_atraso:
            print(f"Usuário '{usuario.nome}' está em atraso e não pode pegar livros.")
            return
        
        emprestimo = Emprestimo(livro, usuario)
        livro.disponivel = False
        self.emprestimos.append(emprestimo)
        print(f"Empréstimo realizado! Devolver até {emprestimo.data_devolucao}")

    def devolver_livro(self, livro, usuario):
        for emprestimo in self.emprestimos:
            if emprestimo.livro == livro and emprestimo.usuario == usuario and not emprestimo.devolvido:
                emprestimo.devolvido = True
                emprestimo.data_devolvido_real = date.today()
                livro.disponivel = True
                usuario.em_atraso = False
                print(f"Livro '{livro.titulo}' devolvido com sucesso!")
                return
        print("Empréstimo não encontrado.")

    def verificar_atrasos(self):
        for emprestimo in self.emprestimos:
            if emprestimo.esta_atrasado():
                emprestimo.usuario.em_atraso = True

    def verificar_atrasos(self):
        for emprestimo in self.emprestimos:
            if emprestimo.esta_atrasado():
                emprestimo.usuario.em_atraso = True

    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.nome.lower() == nome.lower():
                return usuario
        return None

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None
    
    def salvar_dados(self):
        with open("data/livros.json", "w") as f:
            json.dump([livro.to_dict() for livro in self.livros], f, indent=4)

        with open("data/usuarios.json", "w") as f:
            json.dump([usuario.to_dict() for usuario in self.usuarios], f, indent=4)

        with open("data/emprestimos.json", "w") as f:
            json.dump([emprestimo.to_dict() for emprestimo in self.emprestimos], f, indent=4)

    def carregar_dados(self):
        try:
            with open("data/livros.json", "r") as f:
                livros = json.load(f)
                for l in livros:
                    livro = Livro(l["isbn"], l["titulo"], l["autor"], l["ano_publicacao"])
                    livro.disponivel = l["disponivel"]
                    self.livros.append(livro)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        try:
            with open("data/usuarios.json", "r") as f:
                usuarios = json.load(f)
                for u in usuarios:
                    usuario = Usuario(u["nome"], u["telefone"])
                    usuario.matricula = u["matricula"]
                    usuario.em_atraso = u["em_atraso"]
                    Usuario.matriculas_usadas.append(u["matricula"])
                    self.usuarios.append(usuario)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        try:
            with open("data/emprestimos.json", "r") as f:
                emprestimos = json.load(f)
                for e in emprestimos:
                    livro = self.buscar_livro(e["livro"])
                    usuario = self.buscar_usuario(e["usuario"])
                    if livro and usuario:
                        emprestimo = Emprestimo(livro, usuario)
                        emprestimo.data_emprestimo = date.fromisoformat(e["data_emprestimo"])
                        emprestimo.data_devolucao = date.fromisoformat(e["data_devolucao"])
                        emprestimo.data_devolvido_real = date.fromisoformat(e["data_devolucao_real"]) if e["data_devolucao_real"] else None
                        emprestimo.devolvido = e["devolvido"]
                        self.emprestimos.append(emprestimo)
        except (FileNotFoundError, json.JSONDecodeError):
            pass