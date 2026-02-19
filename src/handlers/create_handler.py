import json
import uuid
from datetime import datetime
from aws_lambda_powertools import Logger, Tracer
from src.infrastructure.schemas import TaskCreateSchema
from src.infrastructure.dynamodb_repository import DynamoDBRepository
from src.utils.error_handler import handle_exceptions
from src.utils.response_handler import success_response

logger = Logger()
tracer = Tracer()
repository = DynamoDBRepository()

@logger.inject_lambda_context
@tracer.capture_lambda_handler
@handle_exceptions
def handler(event, context):
    logger.info("Iniciando criação de nova tarefa")
    body = json.loads(event.get("body", "{}"))
    validated_data = TaskCreateSchema(**body)
    
    task_id = str(uuid.uuid4())
    
    task_item = {
        "id": task_id,
        "titulo": validated_data.titulo,
        "descricao": validated_data.descricao,
        "status": validated_data.status,
        "criado_por": validated_data.criado_por,
        "data_criacao": datetime.now().strftime("%d/%m/%Y"),
        "data_conclusao": datetime.now().strftime("%d/%m/%Y") if validated_data.status == "Concluída" else None
    }

    repository.save(task_item)
    logger.info(f"Tarefa criada com sucesso", extra={"task_id": task_id, "titulo": validated_data.titulo})
    return success_response(201, task_item)