variable "aws_region" {
  description = "Região da AWS"
  default     = "sa-east-1"
}

variable "table_name" {
  description = "Nome da tabela no DynamoDB"
  default     = "LawyerTasks"
}