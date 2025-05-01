# AWS Data Lakehouse Pipeline with Airflow and AWS Glue

This project demonstrates an end-to-end pipeline using Airflow to orchestrate an AWS-based lakehouse pipeline: raw data is ingested from S3, transformed using a Glue job, and finalized in a curated S3 bucket.

## Architecture
- **Raw Data Source**: S3 (`my-raw-bucket`)
- **Orchestration**: Airflow
- **Processing**: AWS Glue (PySpark script)
- **Destination**: S3 (`my-curated-bucket`)
- **Infra Provisioning**: Terraform

## How to Run

### 1. Setup Infra
```bash
cd terraform
terraform init
terraform apply
```

### 2. Upload Glue Script
Upload `glue_transform_script.py` to the `aws-glue-scripts` bucket.

### 3. Build and Run Airflow
```bash
docker build -t lakehouse-airflow .
docker run -d -p 8080:8080 lakehouse-airflow
```
Access Airflow UI at `http://localhost:8080` and trigger the DAG.

## DAG Steps
1. **Extract**: Copy raw CSV data to a working S3 path.
2. **Transform**: Trigger Glue ETL Job to transform and move to curated zone.
3. **Load**: Confirmation/log step post Glue transformation.

## Requirements
- AWS CLI configured
- Docker
- Terraform
- Python 3.8+
- AWS Glue script uploaded to S3