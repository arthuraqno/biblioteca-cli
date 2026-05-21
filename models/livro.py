class Livro:
    def __init__(self, isbn, titulo, autor, ano_publicacao):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"[{self.isbn}] {self.titulo} by {self.autor} ({self.ano_publicacao})"
    
    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano_publicacao": self.ano_publicacao,
            "disponivel": self.disponivel
        }
