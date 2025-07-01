from sqlalchemy.orm import Session
from app.models.agendamento import Agendamento
from app.schemas.agendamento import AgendamentoCreate

def criar_agendamento(db: Session, payload: AgendamentoCreate):
    novo = Agendamento(**payload.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return {"id": novo.id, "status": "agendado"}