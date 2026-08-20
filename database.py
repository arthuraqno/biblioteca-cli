from sqlalchemy import create_engine
from base import Base
import os
from dotenv import load_dotenv
from models.emprestimo import Emprestimo
from models.livro import Livro
from models.usuario import Usuario

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
print("Tabelas criadas com sucesso!")