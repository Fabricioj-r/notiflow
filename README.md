# Notiflow 📬


![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)

---

## 📌 Visão Geral do Projeto

Este é o **Notiflow**, uma API RESTful que desenvolvi em Python (FastAPI) para o desafio técnico do Magalu. Com ela, consigo agendar, consultar status e remover comunicações (e-mail, SMS, push, WhatsApp), sempre seguindo os requisitos do desafio: uso obrigatório de **PostgreSQL**, padrão REST, respostas em JSON e testes automatizados.

---

## 🎯 Requisitos Atendidos

- [x] Backend em Python (FastAPI)
- [x] Banco de dados relacional PostgreSQL (sem fallback para SQLite)
- [x] ORM SQLAlchemy 2.x + Alembic para migrações
- [x] Validação e serialização com Pydantic v2
- [x] APIs RESTful, respostas em JSON
- [x] Testes unitários e de integração organizados (Pytest)
- [x] Documentação técnica clara e completa

---

## 🛠️ Tecnologias que utilizei

- Python 3.11+
- FastAPI
- SQLAlchemy 2.x
- Alembic
- Pydantic v2
- PostgreSQL
- Pytest
- python-dotenv

---

## 🏗️ Estrutura de Pastas e Arquitetura

Organizei o projeto para facilitar a manutenção e a escalabilidade. Veja como está estruturado:

```
notiflow/
├── app/
│   ├── crud/           # Funções de acesso ao banco (Create, Read, Delete)
│   │   └── agendamento.py
│   ├── database/       # Configuração da conexão e sessão com o banco
│   │   └── connection.py
│   ├── models/         # Modelos ORM (SQLAlchemy)
│   │   └── agendamento.py
│   ├── routes/         # Endpoints da API (FastAPI)
│   │   └── agendamento.py
│   └── schemas/        # Schemas Pydantic (validação e serialização)
│       └── agendamento.py
├── alembic/            # Migrações do banco de dados
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── tests/
│   ├── unit/           # Testes unitários (lógica isolada)
│   │   ├── test_crud_agendamento.py
│   │   ├── test_enums.py
│   │   └── test_schemas.py
│   └── integration/    # Testes de integração (endpoints e banco real)
│       └── test_agendamentos.py
├── main.py             # Ponto de entrada da aplicação
├── requirements.txt    # Dependências do projeto
├── alembic.ini         # Configuração do Alembic
├── run_tests.bat       # Script para rodar todos os testes
└── README.md           # Documentação principal
```

---

## 💡 Por que escolhi Python e como organizei tudo:

Escolhi Python porque é a linguagem que mais domino e com a qual me sinto mais confortável para entregar soluções rápidas e de qualidade. Gosto muito do FastAPI pela praticidade e da combinação com PostgreSQL, que já tive a oportunidade de usar em outros projetos e que venho aprendendo cada vez mais. Procurei deixar tudo bem organizado, separar os testes (unitários e integração), usar ferramentas modernas e facilitar ao máximo para quem for rodar ou avaliar o projeto.

Sendo bem sincero: eu não tinha muito conhecimento prático em testes unitários antes desse desafio, mas estudei, pesquisei e fiz o máximo para entregar algo que atendesse o que foi pedido. Se encontrar algum ponto a melhorar, vou ficar feliz em receber feedback!

---

## 🚀 Como rodar o Notiflow (local ou Docker):

Quis deixar o Notiflow o mais acessível possível. Por isso, o projeto pode ser executado **localmente** (com Python e PostgreSQL instalados) ou de forma **automatizada via Docker**. 

---

### 1. Clonando o repositório:

```bash
git clone https://github.com/fabriciojunior/notiflow.git
cd notiflow
```

---

### 2. Escolha como rodar: Localmente ou via Docker:

#### **A) Rodando localmente (meu jeito tradicional)**

1. **Crie e ative o ambiente virtual:**
   - **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure o PostgreSQL:**
   - No terminal do PostgreSQL (psql) como superusuário:
     ```sql
     CREATE USER notiflow_user WITH PASSWORD 'minhasenha';
     CREATE DATABASE notiflow_db WITH ENCODING 'UTF8' OWNER notiflow_user;
     GRANT ALL PRIVILEGES ON DATABASE notiflow_db TO notiflow_user;
     ALTER DATABASE notiflow_db OWNER TO notiflow_user;
     \c notiflow_db
     ALTER SCHEMA public OWNER TO notiflow_user;
     GRANT ALL ON SCHEMA public TO notiflow_user;
     GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO notiflow_user;
     GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO notiflow_user;
     ```

4. **Defina as variáveis de ambiente:**
   - **Windows (PowerShell):**
     ```powershell
     $env:PYTHONPATH="C:\Users\Usuario\Desktop\notiflow"
     $env:DATABASE_URL="postgresql+psycopg2://notiflow_user:minhasenha@localhost:5432/notiflow_db?client_encoding=utf8"
     ```
   - **Linux/Mac:**
     ```bash
     export PYTHONPATH=$(pwd)
     export DATABASE_URL="postgresql+psycopg2://notiflow_user:minhasenha@localhost:5432/notiflow_db?client_encoding=utf8"
     ```
   - Ou crie um arquivo `.env` na raiz do projeto:
     ```
     DATABASE_URL=postgresql+psycopg2://notiflow_user:minhasenha@localhost:5432/notiflow_db?client_encoding=utf8
     ```

5. **Rode as migrações:**
   ```bash
   alembic upgrade head
   ```

6. **Inicie a aplicação:**
   ```bash
   uvicorn main:app --reload
   ```
   - Acesse a documentação interativa em [http://localhost:8000/docs](http://localhost:8000/docs)

7. **Rode os testes:**
   - **Testes unitários:**
     ```bash
     pytest tests/unit
     ```
   - **Testes de integração:**
     ```bash
     pytest tests/integration
     ```

---

#### **B) Rodando via Docker (tudo pronto em poucos minutos)**

1. **Suba toda a infraestrutura (banco e app):**
   ```bash
   docker-compose up --build -d
   ```

2. **Acesse a API em:**  
   [http://localhost:8000/docs](http://localhost:8000/docs)

3. **Para rodar migrações ou testes dentro do container:**
   ```bash
   docker-compose exec app alembic upgrade head
   docker-compose exec app pytest tests/integration
   docker-compose exec app pytest tests/unit
   ```

4. **Para parar e remover tudo:**
   ```bash
   docker-compose down -v
   ```

> **Dica:** No Docker, o banco, usuário e permissões já são criados automaticamente. Não precisa configurar nada manualmente!

---

## 🧪 Testes automatizados

Separei os testes em unitários e de integração

### Antes de rodar os testes, lembre de ativar o ambiente virtual:
```bash
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### Para rodar todos os testes:
```bash
./run_tests.bat  # Windows
pytest           # Linux/Mac
```

### Só os testes unitários:
```bash
pytest tests/unit
```

### Só os testes de integração:
```bash
pytest tests/integration
```

- Testes unitários: Valido a lógica isolada (enums, schemas, CRUD).
- Testes de integração: Valido os endpoints e a integração real com o banco PostgreSQL.

> Todos os testes passam com o PostgreSQL configurado. Não tem fallback para SQLite.

---

## 📚 Exemplos de uso dos endpoints

> **Atenção:** O endpoint `/agendamentos/` aceita todos os tipos de comunicação exigidos no desafio através do campo `tipo_comunicacao`. Os valores aceitos são: `email`, `sms`, `push`, `whatsapp`.
> Basta informar o tipo desejado no payload, sem necessidade de endpoints separados.

### Criar agendamento (exemplos para cada tipo)

#### Email
```http
POST /agendamentos
Content-Type: application/json
{
  "data_hora_envio": "2024-07-01T10:00:00",
  "destinatario": "email@exemplo.com",
  "mensagem": "Olá!",
  "tipo_comunicacao": "email"
}
```

#### SMS
```http
POST /agendamentos
Content-Type: application/json
{
  "data_hora_envio": "2024-07-01T10:00:00",
  "destinatario": "+5511999999999",
  "mensagem": "Olá!",
  "tipo_comunicacao": "sms"
}
```

#### Push
```http
POST /agendamentos
Content-Type: application/json
{
  "data_hora_envio": "2024-07-01T10:00:00",
  "destinatario": "user_123",
  "mensagem": "Você ganhou um cupom!",
  "tipo_comunicacao": "push"
}
```

#### WhatsApp
```http
POST /agendamentos
Content-Type: application/json
{
  "data_hora_envio": "2024-07-01T10:00:00",
  "destinatario": "+5511987654321",
  "mensagem": "Bom dia!",
  "tipo_comunicacao": "whatsapp"
}
```

### Consultar status
```http
GET /agendamentos/{id}/status
```

### Remover agendamento
```http
DELETE /agendamentos/{id}
```

---

## 🛠️ Solução de problemas comuns

Se ao rodar as migrações aparecer erro de permissão no schema public, execute no psql como superusuário:

```sql
ALTER DATABASE notiflow_db OWNER TO notiflow_user;
ALTER SCHEMA public OWNER TO notiflow_user;
GRANT ALL ON SCHEMA public TO notiflow_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO notiflow_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO notiflow_user;
```

---

## Considerações Finais

Ao desenvolver este projeto, sempre pensei em facilitar a manutenção e ajudar quem for mexer no código depois. Organizei tudo de forma clara, para que seja fácil entender, modificar e adicionar novas funcionalidades no futuro, como o envio real das mensagens ou outras melhorias que possam surgir.


### Sobre os status dos agendamentos

Cada agendamento pode ter um dos seguintes status:

- **pendente**: Agendamento criado, aguardando envio da comunicação.
- **enviado**: Comunicação enviada com sucesso (previsto para o futuro).
- **erro**: Algum problema ao tentar enviar a comunicação (previsto para o futuro).
- **cancelada**: Agendamento removido/cancelado antes do envio.

> **Nota:** Nesta etapa, só os status "pendente" e "cancelada" são usados de fato, já que o envio real das mensagens ainda não faz parte do escopo. Os outros status já estão previstos para facilitar a evolução do sistema.

**Sobre esta entrega:**  
O desafio pediu só para agendar, consultar status e remover comunicações, salvando no PostgreSQL e com testes. O envio real das mensagens pode ser feito depois, já que a estrutura está pronta pra isso.

---

## 📝 Sobre mim

- Nome: Fabrício Júnior
- Email: fabriciojunior383@gmail.com
- LinkedIn: [linkedin.com/in/fabriciojunior](https://linkedin.com/in/fabriciojunior)
- GitHub: [github.com/Fabricioj-r](https://github.com/Fabricioj-r)

Agradeço pela oportunidade de participar do processo seletivo, estou à disposição para dúvidas e sugestões.