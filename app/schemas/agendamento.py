from pydantic import BaseModel, Field
from pydantic import ConfigDict
from datetime import datetime
from enum import Enum
from typing import Optional

class TipoComunicacaoEnum(str, Enum):
    email = 'email'
    sms = 'sms'
    push = 'push'
    whatsapp = 'whatsapp'

class StatusAgendamentoEnum(str, Enum):
    pendente = 'pendente'
    enviado = 'enviado'
    erro = 'erro'
    cancelado = 'cancelado'

class AgendamentoCreate(BaseModel):
    data_hora_envio: datetime = Field(..., description="Data e hora para o envio da comunicação")
    destinatario: str = Field(..., description="Destinatário da comunicação")
    mensagem: str = Field(..., description="Mensagem a ser entregue")
    tipo_comunicacao: TipoComunicacaoEnum = Field(..., description="Tipo de comunicação")

class AgendamentoResponse(BaseModel):
    id: int
    data_hora_envio: datetime
    destinatario: str
    mensagem: str
    tipo_comunicacao: TipoComunicacaoEnum
    status: StatusAgendamentoEnum

    model_config = ConfigDict(from_attributes=True)

class AgendamentoStatusResponse(BaseModel):
    id: int
    status: StatusAgendamentoEnum

    model_config = ConfigDict(from_attributes=True)