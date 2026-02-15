import json
from datetime import datetime
from aws_lambda_powertools import Logger
from src.infrastructure.dynamodb_repository import DynamoDBRepository
from src.utils.error_handler import handle_exceptions

logger = Logger()
repository = DynamoDBRepository()

@logger.inject_lambda_context
@handle_exceptions
def handler(event, context):
    task_id = event.get("pathParameters", {}).get("id")
    if not task_id:
        raise ValueError("ID da tarefa é obrigatório")

    body = json.loads(event.get("body", "{}"))
    if body.get("status") == "Concluída":
        body["data_conclusao"] = datetime.now().strftime("%d/%m/%Y")
    elif "status" in body:
        body["data_conclusao"] = None
    repository.update(task_id, body)
    return {"statusCode": 200, "body": json.dumps({"message": "Sucesso", "id": task_id})}