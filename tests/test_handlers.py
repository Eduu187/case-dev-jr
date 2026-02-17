import json
from dataclasses import dataclass
from unittest.mock import patch
from src.handlers import update_handler, create_handler

@dataclass
class MockContext:
    function_name: str = "test-function"
    memory_limit_in_mb: int = 128
    invoked_function_arn: str = "arn:aws:lambda:sa-east-1:123456789012:function:test-function"
    aws_request_id: str = "550e8400-e29b-41d4-a716-446655440000"

@patch("src.handlers.update_handler.repository.update")
def test_handler_update_concluida_fills_date(mock_update):
    event = {
        "pathParameters": {"id": "123"},
        "body": json.dumps({"status": "Concluída"})
    }
    
    update_handler.handler(event, MockContext())
    
    args, _ = mock_update.call_args
    assert args[1]["data_conclusao"] is not None 
    assert args[1]["status"] == "Concluída"

@patch("src.handlers.create_handler.repository.save")
def test_handler_create_generates_id_and_date(mock_save):
    event = {
        "body": json.dumps({
            "titulo": "Nova Tarefa",
            "descricao": "Desc",
            "status": "Pendente",
            "criado_por": "User"
        })
    }
    
    response = create_handler.handler(event, MockContext())
    body = json.loads(response["body"])
    
    assert "id" in body
    assert body["data_criacao"] is not None
    assert body["data_conclusao"] is None