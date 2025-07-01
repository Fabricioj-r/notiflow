from fastapi import FastAPI
from app.routes import agendamento

app = FastAPI()

app.include_router(agendamento.router)