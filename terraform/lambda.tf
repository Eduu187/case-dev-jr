resource "aws_lambda_function" "lawyer_api" {
  function_name    = "LawyerApiFunction"
  role             = aws_iam_role.lambda_role.arn
  runtime          = "python3.10"
  
  handler          = "src.handlers.main_handler.handler" 
  
  filename         = "lambda_function_payload.zip"
  source_code_hash = fileexists("lambda_function_payload.zip") ? filebase64sha256("lambda_function_payload.zip") : null
  
  tracing_config {
      mode = "Active"
    }

  environment {
    variables = {
      TABLE_NAME = var.table_name
    }
  }
}