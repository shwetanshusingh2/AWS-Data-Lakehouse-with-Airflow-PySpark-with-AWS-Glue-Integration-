from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator
from datetime import datetime

def create_dag():
    with DAG(
        dag_id="aws_lakehouse_pipeline",
        schedule_interval="@daily",
        start_date=datetime(2024, 1, 1),
        catchup=False
    ) as dag:

        extract = BashOperator(
            task_id="extract_data",
            bash_command="aws s3 cp s3://my-shw-test-bucket123/data.csv s3://aws-glue-temp-bucket/input/data.csv"
        )

        transform = AwsGlueJobOperator(
            task_id="transform_with_glue",
            job_name="glue-transform-job",
            script_location="s3://aws-glue-scripts/glue_transform_script.py",
            region_name="us-west-2",
            iam_role_name="GlueServiceRole",
            num_of_dpus=2,
            create_job_kwargs={
                'GlueVersion': '3.0',
                'ExecutionProperty': {'MaxConcurrentRuns': 1},
                'Command': {
                    'Name': 'glueetl',
                    'ScriptLocation': 's3://aws-glue-scripts/glue_transform_script.py',
                    'PythonVersion': '3'
                },
                'DefaultArguments': {
                    '--TempDir': 's3://aws-glue-temp-bucket/temp/',
                    '--job-language': 'python',
                    '--enable-metrics': ''
                }
            }
        )

        load = BashOperator(
            task_id="load_data",
            bash_command="echo 'Data loaded to curated bucket by Glue Job.'"
        )

        extract >> transform >> load
        return dag

globals()["aws_lakehouse_pipeline"] = create_dag()