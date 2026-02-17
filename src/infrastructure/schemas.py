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
    data_criacao: str
    data_conclusao: Optional[str] = None

class TaskUpdateSchema(BaseModel):
    titulo: Optional[str] = Field(None, min_length=3, max_length=100)
    descricao: Optional[str] = Field(None, max_length=500)
    status: Optional[str] = Field(None, pattern="^(Pendente|Em Andamento|Concluída)$")

    @validator('status')
    def validate_status(cls, v):
        if v is None:
            return v
        allowed = ["Pendente", "Em Andamento", "Concluída"]
        if v not in allowed:
            raise ValueError(f"Status deve ser um de: {allowed}")
        return v

    def dict(self, exclude_none=True, **kwargs):
        return super().dict(exclude_none=True, **kwargs)