from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class TaskCreateSchema(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100)
    descricao: str = Field(..., max_length=500)
    status: str = Field(..., pattern="^(Pendente|Em Andamento|Concluída)$")
    criado_por: str

    @validator('status')
    def validate_status(cls, v):
        allowed = ["Pendente", "Em Andamento", "Concluída"]
        if v not in allowed:
            raise ValueError(f"Status deve ser um de: {allowed}")
        return v

class TaskResponseSchema(TaskCreateSchema):
    id: str
    data_creation: str
    data_conclusao: Optional[str] = None