import functools
from enum import Enum
from aws_lambda_powertools import Logger
from botocore.exceptions import ClientError
from src.utils.response_handler import error_response
from pydantic import ValidationError

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
        except Exception as e:
            return _map_exception_to_response(e)
    return wrapper

def _map_exception_to_response(e):
    error_type = ErrorResponse.INTERNAL_ERROR
    custom_message = None

    if isinstance(e, ValidationError):
        error_type = ErrorResponse.BAD_REQUEST
        errors = e.errors()
        custom_message = "Erro de validação: " + ", ".join(
            [f"'{err['loc'][0]}': {err['msg']}" for err in errors]
        )
    
    elif isinstance(e, ValueError):
        error_type = ErrorResponse.BAD_REQUEST
        custom_message = str(e)
    
    elif isinstance(e, ClientError):
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            error_type = ErrorResponse.NOT_FOUND
    
    return _build_error_response(error_type, custom_message, original_exception=e)

def _build_error_response(error: ErrorResponse, custom_message=None, original_exception=None):
    message = custom_message or error.message
    
    if error == ErrorResponse.INTERNAL_ERROR:
        logger.exception(f"Erro 500: {str(original_exception)}")
    else:
        logger.error(f"Erro {error.code}: {message}")

    return error_response(error.code, message)