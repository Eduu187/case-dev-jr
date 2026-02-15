import json
import functools
from enum import Enum
from aws_lambda_powertools import Logger

logger = Logger()

class ErrorResponse(Enum):
    BAD_REQUEST = (400, "Erro de validação ou parâmetros ausentes.")
    NOT_FOUND = (404, "Tarefa não encontrada.")
    INTERNAL_ERROR = (500, "Erro interno ao processar a requisição.")

    def __init__(self, code, message):
        self.code = code
        self.message = message

def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(event, context):
        try:
            return func(event, context)
        except ValueError as e:
            error_msg = str(e) if str(e) else ErrorResponse.BAD_REQUEST.message
            logger.error(f"Erro 400: {error_msg}")
            return {
                "statusCode": ErrorResponse.BAD_REQUEST.code,
                "body": json.dumps({"error": error_msg})
            }
        except Exception as e:
            logger.exception(f"Erro 500: {str(e)}")
            return {
                "statusCode": ErrorResponse.INTERNAL_ERROR.code,
                "body": json.dumps({"error": ErrorResponse.INTERNAL_ERROR.message})
            }
    return wrapper