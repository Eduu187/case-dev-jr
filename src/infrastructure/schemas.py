from pydantic import BaseModel, Field, field_validator
from typing import Optional

class TaskCreateSchema(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100)
    descricao: str = Field(..., max_length=500)
    status: str = Field(...)
    criado_por: str

    @field_validator('status')
    @classmethod
    def validate_status(cls, v: str):
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
    status: Optional[str] = Field(None)

    @field_validator('status')
    @classmethod
    def validate_status(cls, v: Optional[str]):
        if v is None:
            return v
        allowed = ["Pendente", "Em Andamento", "Concluída"]
        if v not in allowed:
            raise ValueError(f"Status deve ser um de: {allowed}")
        return v