import json
from datetime import datetime
from aws_lambda_powertools import Logger
from src.infrastructure.schemas import TaskUpdateSchema
from src.infrastructure.dynamodb_repository import DynamoDBRepository
from src.utils.error_handler import handle_exceptions
from src.utils.response_handler import success_response

logger = Logger()
repository = DynamoDBRepository()

@logger.inject_lambda_context
@handle_exceptions
def handler(event, context):
    task_id = event.get("pathParameters", {}).get("id")
    if not task_id:
        raise ValueError("ID da tarefa é obrigatório")

    logger.info(f"Iniciando atualização de tarefa", extra={"task_id": task_id})
    body = json.loads(event.get("body", "{}"))
    validated_data = TaskUpdateSchema(**body)
    update_data = validated_data.model_dump(exclude_unset=True)
    
    if update_data.get("status") == "Concluída":
        update_data["data_conclusao"] = datetime.now().strftime("%d/%m/%Y")
    elif "status" in update_data:
        update_data["data_conclusao"] = None
    
    repository.update(task_id, update_data)
    logger.info(f"Tarefa atualizada com sucesso", extra={"task_id": task_id, "campos_atualizados": list(update_data.keys())})
    return success_response(200, {"message": "Sucesso", "id": task_id})