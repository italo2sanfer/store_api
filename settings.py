import os

INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME", "projeto:regiao:instancia")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "pass")  # Secret key
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "mydb")
API_KEY = os.getenv("API_KEY", "Access token") # Secret key