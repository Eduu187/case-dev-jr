import json
from src.infrastructure.dynamodb_repository import DynamoDBRepository
from src.utils.error_handler import handle_exceptions, ErrorResponse

repository = DynamoDBRepository()

@handle_exceptions
def handler(event, context):
    task_id = event.get("pathParameters", {}).get("id")

    if task_id:
        item = repository.get_by_id(task_id)
        if not item:
            return {
                "statusCode": ErrorResponse.NOT_FOUND.code,
                "body": json.dumps({"error": ErrorResponse.NOT_FOUND.message})
            }
        return {"statusCode": 200, "body": json.dumps(item)}

    return {"statusCode": 200, "body": json.dumps(repository.list_all())}