from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL or not DATABASE_URL.startswith("postgresql"):
    # Só levanta o erro ao tentar criar a engine, não na importação
    def raise_db_url_error(*args, **kwargs):
        raise RuntimeError(
            "A variável de ambiente DATABASE_URL deve estar definida e apontar para um banco PostgreSQL. Exemplo: postgresql://usuario:senha@localhost:5432/notiflow_db"
        )
    engine = None
    SessionLocal = raise_db_url_error
else:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Função geradora de sessão para uso com FastAPI (dependência)
def get_db():
    if not SessionLocal or not engine:
        raise RuntimeError(
            "A variável de ambiente DATABASE_URL deve estar definida e apontar para um banco PostgreSQL. Exemplo: postgresql://usuario:senha@localhost:5432/notiflow_db"
        )
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
