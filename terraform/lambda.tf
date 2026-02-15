resource "aws_lambda_function" "create_task" {
  function_name    = "CreateTaskFunction"
  role             = aws_iam_role.lambda_role.arn
  runtime          = "python3.10"
  handler          = "src.handlers.create_handler.handler" 
  filename         = "lambda_function_payload.zip"
  source_code_hash = fileexists("lambda_function_payload.zip") ? filebase64sha256("lambda_function_payload.zip") : null
  environment { variables = { TABLE_NAME = var.table_name } }
}

resource "aws_lambda_function" "get_task" {
  function_name    = "GetTaskFunction"
  role             = aws_iam_role.lambda_role.arn
  runtime          = "python3.10"
  handler          = "src.handlers.get_handler.handler" 
  filename         = "lambda_function_payload.zip"
  source_code_hash = fileexists("lambda_function_payload.zip") ? filebase64sha256("lambda_function_payload.zip") : null
  environment { variables = { TABLE_NAME = var.table_name } }
}

resource "aws_lambda_function" "update_task" {
  function_name    = "UpdateTaskFunction"
  role             = aws_iam_role.lambda_role.arn
  runtime          = "python3.10"
  handler          = "src.handlers.update_handler.handler" 
  filename         = "lambda_function_payload.zip"
  source_code_hash = fileexists("lambda_function_payload.zip") ? filebase64sha256("lambda_function_payload.zip") : null
  environment { variables = { TABLE_NAME = var.table_name } }
}

resource "aws_lambda_function" "delete_task" {
  function_name    = "DeleteTaskFunction"
  role             = aws_iam_role.lambda_role.arn
  runtime          = "python3.10"
  handler          = "src.handlers.delete_handler.handler" 
  filename         = "lambda_function_payload.zip"
  source_code_hash = fileexists("lambda_function_payload.zip") ? filebase64sha256("lambda_function_payload.zip") : null
  environment { variables = { TABLE_NAME = var.table_name } }
}