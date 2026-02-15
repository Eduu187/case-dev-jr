provider "aws" {
  region = "sa-east-1"
}

variable "table_name" {
  default = "LawyerTasks"
}

resource "aws_dynamodb_table" "todo_table" {
  name         = var.table_name
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

resource "aws_iam_role" "lambda_role" {
  name = "lawyer_api_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_policy" "dynamo_policy" {
  name = "LawyerApiDynamoPolicy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action   = ["dynamodb:PutItem", "dynamodb:GetItem", "dynamodb:UpdateItem", "dynamodb:DeleteItem", "dynamodb:Scan"]
      Effect   = "Allow"
      Resource = aws_dynamodb_table.todo_table.arn
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_dynamo" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.dynamo_policy.arn
}

resource "aws_lambda_function" "create_task" {
  function_name = "CreateTaskFunction"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.10"
  
  handler       = "src.handlers.create_handler.handler" 
  filename      = "lambda_function_payload.zip"

  environment {
    variables = {
      TABLE_NAME = var.table_name
    }
  }

  tracing_config {
    mode = "Active"
  }
}

resource "aws_api_gateway_rest_api" "lawyer_api" {
  name        = "LawyerTodoListAPI"
  description = "API para gerenciamento de tarefas de advogados"
}

resource "aws_lambda_permission" "apigw_lambda" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.create_task.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.lawyer_api.execution_arn}/*/*"
}