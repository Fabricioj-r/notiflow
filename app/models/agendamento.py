from sqlalchemy import Column, Integer, String, DateTime, Enum
from app.database.connection import Base
import enum

class TipoComunicacaoEnum(enum.Enum):
    email = 'email'
    sms = 'sms'
    push = 'push'
    whatsapp = 'whatsapp'

class StatusAgendamentoEnum(enum.Enum):
    pendente = 'pendente'
    enviado = 'enviado'
    erro = 'erro'
    cancelado = 'cancelado'

class Agendamento(Base):
    __tablename__ = 'agendamentos'

    id = Column(Integer, primary_key=True, index=True)
    data_hora_envio = Column(DateTime, nullable=False)
    destinatario = Column(String, nullable=False)
    mensagem = Column(String, nullable=False)
    tipo_comunicacao = Column(Enum(TipoComunicacaoEnum), nullable=False)
    status = Column(Enum(StatusAgendamentoEnum), nullable=False, default=StatusAgendamentoEnum.pendente)