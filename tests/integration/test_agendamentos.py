import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.agendamento import Base
from main import app
from app.database import connection

# Cria um banco de dados em memória para os testes
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria as tabelas no banco de dados de teste
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Sobrescreve a dependência do banco na aplicação para usar o banco de teste
app.dependency_overrides[connection.get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_and_teardown():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_criar_agendamento_email():
    payload = {
        "data_hora_envio": "2025-06-05T09:30:00",
        "destinatario": "joao.silva@email.com",
        "mensagem": "Olá João, sua inscrição foi confirmada!",
        "tipo_comunicacao": "email"
    }
    response = client.post("/agendamentos/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] > 0
    assert data["destinatario"] == payload["destinatario"]
    assert data["mensagem"] == payload["mensagem"]
    assert data["tipo_comunicacao"] == payload["tipo_comunicacao"]
    assert data["status"] == "pendente"

def test_criar_agendamento_sms():
    payload = {
        "data_hora_envio": "2025-06-10T14:00:00",
        "destinatario": "+5511999998888",
        "mensagem": "Seu pedido #12345 está a caminho!",
        "tipo_comunicacao": "sms"
    }
    response = client.post("/agendamentos/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["destinatario"] == payload["destinatario"]
    assert data["mensagem"] == payload["mensagem"]
    assert data["tipo_comunicacao"] == payload["tipo_comunicacao"]
    assert data["status"] == "pendente"

def test_criar_agendamento_push():
    payload = {
        "data_hora_envio": "2025-06-15T18:45:00",
        "destinatario": "user_789",
        "mensagem": "Você ganhou um cupom de desconto!",
        "tipo_comunicacao": "push"
    }
    response = client.post("/agendamentos/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["destinatario"] == payload["destinatario"]
    assert data["mensagem"] == payload["mensagem"]
    assert data["tipo_comunicacao"] == payload["tipo_comunicacao"]
    assert data["status"] == "pendente"

def test_criar_agendamento_whatsapp():
    payload = {
        "data_hora_envio": "2025-07-01T08:00:00",
        "destinatario": "+5511987654321",
        "mensagem": "Bom dia! Não esqueça da sua reunião às 10h.",
        "tipo_comunicacao": "whatsapp"
    }
    response = client.post("/agendamentos/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["destinatario"] == payload["destinatario"]
    assert data["mensagem"] == payload["mensagem"]
    assert data["tipo_comunicacao"] == payload["tipo_comunicacao"]
    assert data["status"] == "pendente"

def test_consultar_status_agendamento():
    payload = {
        "data_hora_envio": "2025-06-20T16:00:00",
        "destinatario": "ana.pereira@email.com",
        "mensagem": "Ana, sua entrega está prevista para hoje!",
        "tipo_comunicacao": "email"
    }
    post_resp = client.post("/agendamentos/", json=payload)
    agendamento_id = post_resp.json()["id"]
    response = client.get(f"/agendamentos/{agendamento_id}/status")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == agendamento_id
    assert data["status"] == "pendente"

def test_remover_agendamento():
    payload = {
        "data_hora_envio": "2025-06-25T11:15:00",
        "destinatario": "contato@empresa.com",
        "mensagem": "Sua assinatura foi renovada com sucesso!",
        "tipo_comunicacao": "push"
    }
    post_resp = client.post("/agendamentos/", json=payload)
    agendamento_id = post_resp.json()["id"]
    response = client.delete(f"/agendamentos/{agendamento_id}")
    assert response.status_code == 204
    response = client.get(f"/agendamentos/{agendamento_id}/status")
    assert response.status_code == 404

def test_consultar_agendamento_inexistente():
    response = client.get("/agendamentos/9999/status")
    assert response.status_code == 404

def test_remover_agendamento_inexistente():
    response = client.delete("/agendamentos/9999")
    assert response.status_code == 404 