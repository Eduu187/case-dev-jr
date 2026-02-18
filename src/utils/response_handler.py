import json
from typing import Any, Optional

def build_response(
    status_code: int,
    data: Optional[Any] = None,
    error_message: Optional[str] = None
) -> dict:
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }
    
    if error_message:
        body = json.dumps({"error": error_message}, ensure_ascii=False)
    elif data is not None:
        body = json.dumps(data) if not isinstance(data, str) else data
    else:
        body = ""
    
    return {
        "statusCode": status_code,
        "headers": headers,
        "body": body
    }


def success_response(status_code: int, data: Any) -> dict:
    return build_response(status_code, data=data)


def error_response(status_code: int, message: str) -> dict:
    return build_response(status_code, error_message=message)
