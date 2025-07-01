import pytest
from app.schemas.agendamento import AgendamentoCreate, TipoComunicacaoEnum
from datetime import datetime


def test_agendamento_create_schema_valido():
    agendamento = AgendamentoCreate(
        data_hora_envio=datetime(2025, 6, 5, 9, 30),
        destinatario='joao@email.com',
        mensagem='Mensagem de teste',
        tipo_comunicacao=TipoComunicacaoEnum.email
    )
    assert agendamento.destinatario == 'joao@email.com'
    assert agendamento.tipo_comunicacao == TipoComunicacaoEnum.email


def test_agendamento_create_schema_invalido():
    with pytest.raises(ValueError):
        AgendamentoCreate(
            data_hora_envio='data_invalida',
            destinatario='joao@email.com',
            mensagem='Mensagem de teste',
            tipo_comunicacao=TipoComunicacaoEnum.email
        ) 