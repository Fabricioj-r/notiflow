from app.models.agendamento import TipoComunicacaoEnum, StatusAgendamentoEnum

def test_tipo_comunicacao_enum_values():
    assert TipoComunicacaoEnum.email.value == 'email'
    assert TipoComunicacaoEnum.sms.value == 'sms'
    assert TipoComunicacaoEnum.push.value == 'push'
    assert TipoComunicacaoEnum.whatsapp.value == 'whatsapp'

def test_status_agendamento_enum_values():
    assert StatusAgendamentoEnum.pendente.value == 'pendente'
    assert StatusAgendamentoEnum.enviado.value == 'enviado'
    assert StatusAgendamentoEnum.erro.value == 'erro'
    assert StatusAgendamentoEnum.cancelado.value == 'cancelado' 