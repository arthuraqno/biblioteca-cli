from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from base import Base

class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    autor = Column(String(100), nullable=False)
    ano_publicacao = Column(Integer)
    disponivel = Column(Boolean)
    
    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"[{self.id}] {self.titulo} | {self.autor} | Ano: {self.ano_publicacao} | {status}"