from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from base import Base
from datetime import date

class Emprestimo(Base):
    __tablename__ = "emprestimos"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    livro_id = Column(Integer, ForeignKey("livros.id"))
    data_emprestimo = Column(Date, nullable=False, default=date.today)
    data_devolucao = Column(Date, nullable=False)
    devolvido = Column(Boolean)
    data_devolucao_real = Column(Date, nullable=True)

    usuario = relationship("Usuario")
    livro = relationship("Livro")

    