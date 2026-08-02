from sqlalchemy.orm import Session
from models.livro import Livro
from models.usuario import Usuario
from models.emprestimo import Emprestimo
from database import engine
from datetime import date, timedelta

class Biblioteca:
    def cadastrar_livros(self,titulo, autor, ano_publicacao, disponivel):
        with Session(engine) as session:
            livro = Livro(
                titulo = titulo,
                autor = autor,
                ano_publicacao = ano_publicacao,
                disponivel = disponivel)
            session.add(livro)
            session.commit()
            print(f"{titulo} adcionado a biblioteca")

    def cadastrar_usuarios(self, nome, telefone, matricula, em_atraso):
        with Session(engine) as session:
            usuario = Usuario(
                nome = nome,
                telefone = telefone,
                matricula = matricula,
                em_atraso = em_atraso)
            session.add(usuario)
            session.commit()
            print(f"{nome} adcionado ao sistema")

    def listar_livros(self):
        with Session(engine) as session:
            livros = session.query(Livro).all()
            if livros:
                for livro in livros:
                    print(livro)
            else:
                print("Não ha livros cadastrados")

    def buscar_livros(self, titulo):
        with Session(engine) as session:
            livro = session.query(Livro).filter(Livro.titulo.ilike(titulo)).first()
            return livro

    def buscar_usuario(self, nome):
        with Session(engine) as session:
            usuario = session.query(Usuario).filter(Usuario.nome.ilike(nome)).first()
            return usuario

    def emprestar_livro(self, titulo, nome):
        with Session(engine) as session:
            livro = session.query(Livro).filter(Livro.titulo.ilike(titulo)).first()
            usuario= session.query(Usuario).filter(Usuario.nome.ilike(nome)).first()
            if livro is None:
                print("Este livro não está cadastrado!")
                return
            if usuario is None:
                print("Usuario não encontrado!")
                return
            if livro.disponivel == False:
                print("Este livro ja esta sendo usado!")
                return
            if usuario.em_atraso == True:
                print("Usurio possui um livro em atraso!")
                return
            livro.disponivel = False
            emprestimo = Emprestimo(
                livro_id = livro.id,
                usuario_id = usuario.id,
                data_emprestimo = date.today(),
                data_devolucao = date.today() + timedelta(days=14),
                devolvido = False,
                data_devolucao_real = None)
            session.add(emprestimo)
            session.commit()
            print("Emprestimo realizado com sucesso!")

    def devolver_livro(self, titulo, nome):
        with Session(engine) as session:
            livro = session.query(Livro).filter(Livro.titulo.ilike(titulo)).first()
            usuario = session.query(Usuario).filter(Usuario.nome.ilike(nome)).first()
            if livro is None:
                print("Este livro não está cadastrado!")
                return
            if usuario is None:
                print("Usuario não encontrado!")
                return
            emprestimo = session.query(Emprestimo).filter(
                Emprestimo.livro_id == livro.id,
                Emprestimo.usuario_id == usuario.id,
                Emprestimo.devolvido == False
            ).first()
            if emprestimo is None:
                print("Nenhum empréstimo ativo encontrado!")
                return
            emprestimo.devolvido = True
            emprestimo.data_devolucao_real = date.today()
            livro.disponivel = True
            session.commit()
            print(f"Livro '{livro.titulo}' devolvido com sucesso!")
            
    def verificar_atrasos(self):
        with Session(engine) as session:
            emprestimo_atrasados = session.query(Emprestimo).filter(
                Emprestimo.devolvido == False, 
                Emprestimo.data_devolucao < date.today()).all()
            for emprestimo in emprestimo_atrasados:   
                emprestimo.usuario.em_atraso = True
                print(f"Usuário {emprestimo.usuario.nome} está em atraso!")
        
        session.commit()
        
    def listar_usuarios(self):
        with Session(engine) as session:
            usuarios = session.query(Usuario).all()
            if usuarios:
                for usuario in usuarios:
                    print(usuario)
            else:
                print("Não ha usuarios cadastrados")
                
            
                

