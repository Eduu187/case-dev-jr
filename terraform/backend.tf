terraform {
  backend "s3" {
    bucket  = "lawyer-api-tfstate-storage"
    key     = "lawyer-api/terraform.tfstate"
    region  = "sa-east-1"
    encrypt = true
  }
}