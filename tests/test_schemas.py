import pytest
from pydantic import ValidationError
from src.infrastructure.schemas import TaskCreateSchema, TaskUpdateSchema

def test_task_create_valid_status():
    data = {
        "titulo": "Tarefa Teste",
        "descricao": "Descricao",
        "status": "Pendente",
        "criado_por": "Dono"
    }
    schema = TaskCreateSchema(**data)
    assert schema.status == "Pendente"

def test_task_create_invalid_status():
    data = {
        "titulo": "Tarefa Teste",
        "descricao": "Descricao",
        "status": "Inexistente",
        "criado_por": "Dono"
    }
    with pytest.raises(ValidationError) as excinfo:
        TaskCreateSchema(**data)
    assert "Status deve ser um de:" in str(excinfo.value)

def test_task_update_invalid_title_length():
    with pytest.raises(ValidationError):
        TaskUpdateSchema(titulo="Ab")