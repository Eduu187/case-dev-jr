import json
from src.handlers import create_handler, get_handler, update_handler, delete_handler


def handler(event, context):
    http_method = event.get("httpMethod")

    if http_method == "POST":
        return create_handler.handler(event, context)
    elif http_method == "GET":
        return get_handler.handler(event, context)
    elif http_method == "PUT":
        return update_handler.handler(event, context)
    elif http_method == "DELETE":
        return delete_handler.handler(event, context)
    return {
        "statusCode": 405,
        "body": json.dumps({"message": "Method Not Allowed"})
    }