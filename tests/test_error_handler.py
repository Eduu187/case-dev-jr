import json
from src.utils.error_handler import handle_exceptions, ErrorResponse
from botocore.exceptions import ClientError

def test_handle_exceptions_value_error():
    @handle_exceptions
    def mock_func(event, context):
        raise ValueError("Erro de validação customizado")
    
    response = mock_func({}, None)
    assert response["statusCode"] == 400
    assert "Erro de validação customizado" in response["body"]

def test_handle_exceptions_dynamo_not_found():
    @handle_exceptions
    def mock_func(event, context):
        error_response = {"Error": {"Code": "ConditionalCheckFailedException"}}
        raise ClientError(error_response, "UpdateItem")
    
    response = mock_func({}, None)
    assert response["statusCode"] == 404
    assert ErrorResponse.NOT_FOUND.message in response["body"]