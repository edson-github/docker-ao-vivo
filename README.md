# Projeto Aprendizado Docker

Este projeto é um exemplo de aplicação Streamlit para visualização de dados de vendas, com suporte para execução em um ambiente Docker.

## Pré-requisitos

- [Docker](https://www.docker.com/) instalado na máquina.

## Como executar a aplicação

### 1. Construir a imagem Docker

No terminal, navegue até o diretório do projeto e execute o comando abaixo para construir a imagem Docker:

```bash
docker build -t sales-dashboard .


## Construcao do banco de dados POSTGRESQL no Docker comando de uma linha apenas

docker run --name postgres-container -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=aprendizado -p 5432:5432 -d postgres:15