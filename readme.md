# FastAPI User API

API REST desenvolvida com FastAPI para cadastro de usuários, utilizando SQLite como banco de dados e SQLAlchemy como ORM.

## Descrição

Este projeto foi criado para demonstrar como montar uma API simples em FastAPI com:

- cadastro de usuários
- validação de dados com Pydantic
- persistência em SQLite
- documentação automática com Swagger
- estrutura organizada por módulos

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Estrutura do projeto

```bash
api-FastAPI-main/
├── app/
│   ├── main.py
│   ├── controllers/
│   ├── database/
│   ├── models/
│   ├── routes/
│   └── schemas/
├── requirements.txt
├── readme.md
├── database.db
└── venv/
```

## Requisitos

- Python 3.10 ou superior
- pip
- virtualenv (opcional, mas recomendado)

## Instalação

Clone o repositório e acesse a pasta do projeto:

```bash
git clone <url-do-repositorio>
cd api-FastAPI-main
```

Crie e ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

Instale as dependências:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Execução

Inicie a API com o comando:

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Endpoints

### GET /

Retorna uma mensagem de confirmação de que a API está funcionando.

### POST /users/

Cria um novo usuário.

Body de exemplo:

```json
{
  "name": "João Silva",
  "email": "joao@email.com",
  "password": "123456"
}
```

Resposta esperada:

```json
{
  "id": 1,
  "name": "João Silva",
  "email": "joao@email.com"
}
```

## Observações

- A tabela `users` é criada automaticamente quando a aplicação inicia.
- O banco de dados SQLite será gerado na raiz do projeto como `database.db`.
- A documentação interativa pode ser acessada em `/docs`.

## Licença

Este projeto está disponível para fins educacionais e de estudo.

---

Se quiser, também posso criar uma versão mais completa com:

- README em inglês
- badges do GitHub
- seção de exemplos de requisições com cURL
- imagem de arquitetura e fluxos da API
