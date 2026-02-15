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
        
    repository.delete(task_id)
    return {"statusCode": 204, "body": ""}