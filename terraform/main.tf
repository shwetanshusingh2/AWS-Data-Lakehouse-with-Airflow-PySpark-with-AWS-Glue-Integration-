provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "raw" {
  bucket = "my-raw-bucket"
}

resource "aws_s3_bucket" "curated" {
  bucket = "my-curated-bucket"
}

resource "aws_s3_bucket" "glue_temp" {
  bucket = "aws-glue-temp-bucket"
}

resource "aws_s3_bucket" "glue_scripts" {
  bucket = "aws-glue-scripts"
}

resource "aws_iam_role" "glue_service_role" {
  name = "GlueServiceRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Principal = {
        Service = "glue.amazonaws.com"
      },
      Effect = "Allow",
      Sid = ""
    }]
  })
  managed_policy_arns = [
    "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
  ]
}