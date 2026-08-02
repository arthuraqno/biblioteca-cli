from sqlalchemy import Integer, String, Column, Boolean
from base import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(50), nullable=False)
    matricula = Column(Integer, nullable=False)
    em_atraso = Column(Boolean)
    
    
    def __str__(self):
        status = "Em atraso" if self.em_atraso else "Regular"
        return f"[{self.id}] {self.nome} | Tel: {self.telefone} | Matrícula: {self.matricula} | {status}"