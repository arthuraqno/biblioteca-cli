from sqlalchemy import create_engine
from base import Base
from models.emprestimo import Emprestimo
from models.livro import Livro
from models.usuario import Usuario


engine = create_engine(
    "postgresql://postgres:104248652@localhost:5432/biblioteca_db"
)

Base.metadata.create_all(engine)