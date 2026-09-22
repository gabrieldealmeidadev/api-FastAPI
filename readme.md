# API FastAPI de Usuários

API REST para gerenciamento de usuários, desenvolvida com FastAPI, SQLAlchemy e SQLite. O projeto implementa um CRUD completo com validação de dados e documentação automática via Swagger/OpenAPI.

## 🧩 Descrição

Esta API permite:

- cadastrar usuários
- listar todos os usuários
- buscar um usuário por ID
- atualizar dados do usuário
- excluir usuários

A estrutura foi organizada em módulos para facilitar manutenção e expansão do projeto.

## 🚀 Tecnologias utilizadas

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## 📁 Estrutura do projeto

```bash
api-FastAPI/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── controllers/
│   │   └── user_controller.py
│   ├── database/
│   │   └── database.py
│   ├── models/
│   │   └── user_model.py
│   ├── routes/
│   │   └── user_routes.py
│   └── schemas/
│       └── user_schema.py
├── requirements.txt
├── readme.md
├── database.db
├── venv/
└── .gitignore
```

## ✅ Requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python 3.10 ou superior
- pip
- ambiente virtual (opcional, mas recomendado)

## 🔧 Instalação

Clone o repositório:

```bash
git clone <url-do-repositorio>
cd api-FastAPI
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

## ▶️ Execução

Para rodar a aplicação, execute:

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## 🧾 Modelos e validação

O modelo de usuário contém os seguintes campos:

```python
id: int
name: str
email: str
password: str
```

A resposta da API não expõe a senha do usuário. A schema de resposta inclui somente:

```python
id: int
name: str
email: str
```

## CRUD completo

### 1) GET /

Retorna uma mensagem de confirmação de que a API está funcionando.

Exemplo de resposta:

```json
{
  "message": "API funcionando!"
}
```

### 2) GET /users/

Lista todos os usuários cadastrados.

Exemplo de resposta:

```json
[
  {
    "id": 1,
    "name": "João Silva",
    "email": "joao@email.com"
  },
  {
    "id": 2,
    "name": "Maria Souza",
    "email": "maria@email.com"
  }
]
```

### 3) GET /users/{user_id}

Busca um usuário específico pelo ID.

Exemplo:

```http
GET /users/1
```

Resposta:

```json
{
  "id": 1,
  "name": "João Silva",
  "email": "joao@email.com"
}
```

Se o usuário não existir, a API retorna status `404` com a mensagem:

```json
{
  "detail": "User not found"
}
```

### 4) POST /users/

Cria um novo usuário.

Body da requisição:

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

### 5) PUT /users/{user_id}

Atualiza os dados de um usuário existente.

Exemplo de requisição:

```http
PUT /users/1
```

Body:

```json
{
  "name": "João Silva Atualizado",
  "email": "joao.novo@email.com",
  "password": "654321"
}
```

Resposta:

```json
{
  "id": 1,
  "name": "João Silva Atualizado",
  "email": "joao.novo@email.com"
}
```

### 6) DELETE /users/{user_id}

Remove um usuário pelo ID.

Exemplo:

```http
DELETE /users/1
```

Resposta de sucesso:

```json
{
  "message": "User deleted successfully"
}
```

Se o usuário não existir, a API retorna `404`.

## 🗂️ Banco de dados

O projeto utiliza SQLite e o banco é gerado localmente no arquivo:

```bash
database.db
```

A tabela `users` é criada automaticamente ao iniciar a aplicação.

## 📌 Observações

- A documentação interativa da API pode ser acessada em `/docs`.
- A senha do usuário é armazenada no banco, mas não é retornada nas respostas da API.
- O projeto pode ser expandido para incluir autenticação, paginação, filtros e testes automatizados.

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais e de estudo.

---

Se quiser, posso também criar uma versão deste README em inglês ou adicionar exemplos com cURL, Postman e Swagger.
