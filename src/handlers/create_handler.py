import json
import uuid
from datetime import datetime
from aws_lambda_powertools import Logger
from src.infrastructure.schemas import TaskCreateSchema
from src.infrastructure.dynamodb_repository import DynamoDBRepository
from src.utils.error_handler import handle_exceptions

logger = Logger()
repository = DynamoDBRepository()

@logger.inject_lambda_context
@handle_exceptions
def handler(event, context):
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
        "data_conclusao": None 
    }

    repository.save(task_item)
    return {"statusCode": 201, "body": json.dumps(task_item)}