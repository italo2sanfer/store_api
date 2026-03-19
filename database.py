import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from google.cloud.sql.connector import Connector

INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME", "projeto:regiao:instancia")
DB_USER = os.getenv("DB_USER", "usuario")
DB_PASSWORD = os.getenv("DB_PASSWORD", "senha123")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "meubanco")

# Inicializa o Conector
connector = Connector()

def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pg8000", # ou "pymysql" para MySQL
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME
    )
    return conn

engine = create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
Base = declarative_base()

def init_db():
    # Cria as tabelas se não existirem
    import models  # noqa: F401

    Base.metadata.create_all(bind=engine)