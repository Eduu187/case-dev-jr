from aws_lambda_powertools import Logger
from src.infrastructure.dynamodb_repository import DynamoDBRepository
from src.utils.error_handler import handle_exceptions, ErrorResponse
from src.utils.response_handler import success_response, error_response

logger = Logger()
repository = DynamoDBRepository()

@logger.inject_lambda_context
@handle_exceptions
def handler(event, context):
    path_params = event.get("pathParameters") or {}
    query_params = event.get("queryStringParameters") or {}
    
    task_id = path_params.get("id")
    status_filter = query_params.get("status")

    if task_id:
        return handler_id(task_id)
    if status_filter:
        return handler_status(status_filter)
    return handler_all()

def handler_id(task_id):
    logger.info(f"Buscando tarefa por ID", extra={"task_id": task_id})
    item = repository.get_by_id(task_id)
    
    if not item:
        logger.warning(f"Tarefa não encontrada", extra={"task_id": task_id})
        return error_response(ErrorResponse.NOT_FOUND.code, ErrorResponse.NOT_FOUND.message)
    
    logger.info(f"Tarefa encontrada com sucesso", extra={"task_id": task_id})
    return success_response(200, item)

def handler_status(status):
    logger.info(f"Filtrando tarefas por status", extra={"status": status})
    items = repository.list_by_status(status)
    
    logger.info(f"Total de tarefas encontradas", extra={"status": status, "count": len(items)})
    return success_response(200, items)

def handler_all():
    logger.info("Listando todas as tarefas")
    items = repository.list_all()
    
    logger.info(f"Total de tarefas retornadas", extra={"count": len(items)})
    return success_response(200, items)