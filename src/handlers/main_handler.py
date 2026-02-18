from aws_lambda_powertools import Logger
from src.handlers import create_handler, get_handler, update_handler, delete_handler
from src.utils.response_handler import error_response

logger = Logger()

@logger.inject_lambda_context
def handler(event, context):
    http_method = event.get("httpMethod")
    logger.info(f"Requisição recebida", extra={"http_method": http_method})

    if http_method == "POST":
        return create_handler.handler(event, context)
    elif http_method == "GET":
        return get_handler.handler(event, context)
    elif http_method == "PUT":
        return update_handler.handler(event, context)
    elif http_method == "DELETE":
        return delete_handler.handler(event, context)
    
    logger.warning(f"Método HTTP não suportado", extra={"http_method": http_method})
    return error_response(405, "Method Not Allowed")