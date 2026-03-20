import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from google.cloud.sql.connector import Connector

INSTANCE_CONNECTION_NAME = settings.INSTANCE_CONNECTION_NAME
DB_USER = settings.DB_USER
DB_PASSWORD = settings.DB_PASSWORD
DB_HOST = settings.DB_HOST
DB_PORT = settings.DB_PORT
DB_NAME = settings.DB_NAME

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