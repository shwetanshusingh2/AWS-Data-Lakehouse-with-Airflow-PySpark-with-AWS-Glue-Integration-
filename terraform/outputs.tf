output "raw_bucket" {
  value = aws_s3_bucket.raw.bucket
}

output "curated_bucket" {
  value = aws_s3_bucket.curated.bucket
}

output "glue_temp_bucket" {
  value = aws_s3_bucket.glue_temp.bucket
}

output "glue_scripts_bucket" {
  value = aws_s3_bucket.glue_scripts.bucket
}