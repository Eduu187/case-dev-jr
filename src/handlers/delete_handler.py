import json
from aws_lambda_powertools import Logger
from src.infrastructure.dynamodb_repository import DynamoDBRepository
from src.utils.error_handler import handle_exceptions, ErrorResponse

logger = Logger()
repository = DynamoDBRepository()

@logger.inject_lambda_context
@handle_exceptions
def handler(event, context):
    task_id = event.get("pathParameters", {}).get("id")
    if not task_id:
        raise ValueError("ID da tarefa é obrigatório")
    
    logger.info(f"Iniciando deleção de tarefa", extra={"task_id": task_id})
    item = repository.get_by_id(task_id)
    if not item:
        logger.warning(f"Tentativa de deletar tarefa inexistente", extra={"task_id": task_id})
        return {
            "statusCode": ErrorResponse.NOT_FOUND.code,
            "body": json.dumps({"error": ErrorResponse.NOT_FOUND.message})
        }
    
    repository.delete(task_id)
    logger.info(f"Tarefa deletada com sucesso", extra={"task_id": task_id})
    return {"statusCode": 204, "body": ""}