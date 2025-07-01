# Notiflow 📬

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)

## 📌 Descrição do Projeto

O **Notiflow** é uma API que desenvolvi para facilitar o agendamento, consulta e remoção de notificações. Com ela, posso criar, visualizar e gerenciar agendamentos de notificações, além de simular o envio com base na data e hora definida.

## 📝 Por que escolhi Python?

Escolhi Python porque é a linguagem que mais domino e com a qual me sinto confortável para entregar soluções robustas, ágeis e de qualidade. Além disso, o ecossistema Python oferece ótimas ferramentas para APIs REST, testes e automação, o que agiliza o desenvolvimento e garante confiabilidade.

## 🚀 Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [PostgreSQL](https://www.postgresql.org/) (ou SQLite para testes locais)
- [Pytest](https://docs.pytest.org/)

---

## 🧪 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/notiflow.git
cd notiflow
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
.\venv\Scripts\activate   # Windows
# ou
source venv/bin/activate # Linux/Mac
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a variável de ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
DATABASE_URL=sqlite:///./database.db
```

> 💡 Se preferir, pode usar PostgreSQL:  
> `DATABASE_URL=postgresql://usuario:senha@localhost:5432/notiflow_db`

---

## 🛠️ Rodando as Migrações

Para criar o banco de dados e as tabelas, execute:

```bash
alembic upgrade head
```

---

## ▶️ Executando a Aplicação

```bash
uvicorn main:app --reload
```

Acesse [http://localhost:8000/docs](http://localhost:8000/docs) para ver a documentação interativa da API.

---

## ✅ Executando os Testes

### Para rodar todos os testes (unitários e integração)

No Windows, basta executar:

```sh
run_tests.bat
```

### Para rodar apenas os testes unitários

```sh
pytest tests/unit --disable-warnings -v
```

### Para rodar apenas os testes de integração

```sh
pytest tests/integration --disable-warnings -v
```

---

## 📄 Estrutura de Pastas

```
notiflow/
├── app/
│   ├── crud/
│   ├── database/
│   ├── models/
│   ├── routes/
│   └── schemas/
├── tests/
│   ├── integration/
│   └── unit/
├── alembic/
├── alembic.ini
├── .env.example
├── requirements.txt
├── run_tests.bat
├── README.md
└── main.py
```

---

## 💡 Funcionalidades que implementei para o desafio

- [x] CRUD de agendamentos com data/hora, destinatário, mensagem e tipo de comunicação.
- [x] Endpoint para agendar envio de comunicação.
- [x] Endpoint para consultar status do agendamento.
- [x] Endpoint para remover agendamento.
- [x] Testes unitários e de integração organizados.
- [x] Uso de SQLite para facilitar execução local (ou PostgreSQL).
- [x] Arquivo `.env` para configurações seguras.
- [x] Documentação clara de como executar o projeto.

---

## 🧠 Extras e Boas Práticas

- Tipagem completa com Python
- Padronização de código
- Testes isolados com override de dependência do banco de dados
- Código compatível com ambientes Linux, Windows e CI/CD
- Separação clara entre testes unitários e de integração

---

## 📜 Licença

Este projeto está licenciado sob o modelo de código aberto [MIT License](LICENSE).

---

## 📫 Contato

Desenvolvido por mim, **Fabrício Júnior**  
Email: fabriciojunior383@gmail.com  
LinkedIn: [linkedin.com/in/fabriciojunior](https://linkedin.com/in/fabriciojunior)

---

Agradeço pela oportunidade de participar do processo seletivo! Se tiver qualquer dúvida ou sugestão, estou à disposição para conversar.
