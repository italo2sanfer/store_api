#!/usr/bin/env bash
set -e

echo "Aguardando o banco de dados em ${DB_HOST}:${DB_PORT}..."

# Espera o banco ficar disponível
while ! nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 1
done

echo "Banco de dados disponível. Iniciando aplicação..."

# Executa o servidor
exec uvicorn main:app --host 0.0.0.0 --port "${APP_PORT}"