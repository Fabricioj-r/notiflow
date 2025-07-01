from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.schemas.agendamento import AgendamentoCreate, AgendamentoResponse, AgendamentoStatusResponse, StatusAgendamentoEnum
from app.models.agendamento import Agendamento, StatusAgendamentoEnum as StatusAgendamentoEnumModel
from app.database.connection import engine, Base
from sqlalchemy.orm import sessionmaker

router = APIRouter(prefix="/agendamentos", tags=["Agendamentos"])

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependência para obter a sessão do banco

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AgendamentoResponse, status_code=status.HTTP_201_CREATED)
def criar_agendamento(agendamento: AgendamentoCreate, db: Session = Depends(get_db)):
    """
    Cria um novo agendamento de comunicação (email, sms, push ou whatsapp).
    Salva o agendamento no banco de dados com status 'pendente'.
    """
    novo_agendamento = Agendamento(
        data_hora_envio=agendamento.data_hora_envio,
        destinatario=agendamento.destinatario,
        mensagem=agendamento.mensagem,
        tipo_comunicacao=agendamento.tipo_comunicacao,
        status=StatusAgendamentoEnumModel.pendente
    )
    db.add(novo_agendamento)
    db.commit()
    db.refresh(novo_agendamento)
    return novo_agendamento

@router.get("/{agendamento_id}/status", response_model=AgendamentoStatusResponse)
def consultar_status_agendamento(agendamento_id: int, db: Session = Depends(get_db)):
    """
    Consulta o status de um agendamento de comunicação pelo ID.
    Retorna 404 se o agendamento não existir.
    """
    agendamento = db.query(Agendamento).filter(Agendamento.id == agendamento_id).first()
    if not agendamento:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return agendamento

@router.delete("/{agendamento_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_agendamento(agendamento_id: int, db: Session = Depends(get_db)):
    """
    Remove um agendamento de comunicação pelo ID.
    Retorna 404 se o agendamento não existir.
    """
    agendamento = db.query(Agendamento).filter(Agendamento.id == agendamento_id).first()
    if not agendamento:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    db.delete(agendamento)
    db.commit()
    return None