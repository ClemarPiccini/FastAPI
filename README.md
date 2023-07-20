# API utilizando FastAPI 

## DATABASE:

*MySQL*

## FRAMEWORK:

*Docker Compose*

### Passos para executar o codigo:

-criar arquivo .env na raiz com as seguintes informações:

MYSQL_DATABASE="database"  
MYSQL_USER="user"  
MYSQL_PASSWORD="password"  
MYSQL_ROOT_PASSWORD="password"  
MYSQL_PORT= 3306  
ADMINER_PORT= 8001

-abrir um terminal e executar o comando:

```docker compose up```

-abrir novo terminal no diretorio app e executar o comando:

```uvicorn main:app --reload```