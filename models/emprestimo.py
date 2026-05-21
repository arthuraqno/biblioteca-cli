from datetime import date, timedelta

class Emprestimo:
    def __init__(self, livro, usuario):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = date.today()
        self.data_devolucao = self.data_emprestimo + timedelta(days=14)
        self.devolvido = False
        self.data_devolucao_real = None

    
    def esta_atrasado(self):
        if self.devolvido:
            return False
        return date.today() > self.data_devolucao
    
    def __str__(self):
        status = "Devolvido" if self.devolvido else ("Atrasado" if self.esta_atrasado() else "Ativo")
        return(
            f"Livro: {self.livro.titulo}\n"
            f"Usuário: {self.usuario.nome}\n"
            f"Emprestado em: {self.data_emprestimo}\n"
            f"Devolver até: {self.data_devolucao}\n"
            f"Status: {status}"
        )
    
    def to_dict(self):
        return {
            "usuario": self.usuario.nome, 
            "livro": self.livro.titulo,
            "data_emprestimo": str(self.data_emprestimo),
            "data_devolucao": str(self.data_devolucao),
            "data_devolucao_real": str(self.data_devolucao_real) if self.data_devolucao_real else None,
            "devolvido": self.devolvido
        }

