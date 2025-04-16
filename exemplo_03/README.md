# Arquivo com instruções para criação do PostgreSQL no Docker

Este exemplo demonstra como configurar e acessar um banco de dados PostgreSQL utilizando Docker.

## Passos para criar o banco de dados PostgreSQL

### 1. Criar o container PostgreSQL

Execute o seguinte comando no terminal para criar e iniciar o container:

```bash
docker run --name postgres-container -e POSTGRES_USER=user_data -e POSTGRES_PASSWORD=nova_senha -e POSTGRES_DB=aprendizado -p 5432:5432 -d postgres:15

```bash
docker exec -it postgres-container psql -U admin -d aprendizado

CREATE DATABASE meu_banco;

\c meu_banco


CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    idade INT,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO clientes (nome, email, idade) VALUES
('João Silva', 'joao@email.com', 30),
('Maria Oliveira', 'maria@email.com', 25),
('Carlos Santos', 'carlos@email.com', 40);

SELECT * FROM clientes;

