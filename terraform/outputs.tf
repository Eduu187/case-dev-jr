output "api_url" {
  description = "URL base da API"
  value       = "${aws_api_gateway_deployment.deployment.invoke_url}/tasks"
}