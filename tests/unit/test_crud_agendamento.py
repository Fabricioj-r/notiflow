import pytest
from unittest.mock import MagicMock
from app.crud.agendamento import criar_agendamento
from app.schemas.agendamento import AgendamentoCreate, TipoComunicacaoEnum
from datetime import datetime

class FakeDB:
    def __init__(self):
        self.added = None
        self.committed = False
        self.refreshed = None
    def add(self, obj):
        self.added = obj
    def commit(self):
        self.committed = True
    def refresh(self, obj):
        self.refreshed = obj

class FakeAgendamento:
    def __init__(self, **kwargs):
        self.id = 1
        for k, v in kwargs.items():
            setattr(self, k, v)


def test_criar_agendamento():
    payload = AgendamentoCreate(
        data_hora_envio=datetime(2025, 6, 5, 9, 30),
        destinatario='joao@email.com',
        mensagem='Mensagem de teste',
        tipo_comunicacao=TipoComunicacaoEnum.email
    )
    db = FakeDB()
    # Monkeypatch Agendamento para usar FakeAgendamento
    import app.crud.agendamento as crud_mod
    original_agendamento = crud_mod.Agendamento
    crud_mod.Agendamento = FakeAgendamento
    try:
        result = criar_agendamento(db, payload)
        assert result['id'] == 1
        assert result['status'] == 'agendado'
        assert db.added.destinatario == 'joao@email.com'
        assert db.committed is True
        assert db.refreshed.id == 1
    finally:
        crud_mod.Agendamento = original_agendamento 