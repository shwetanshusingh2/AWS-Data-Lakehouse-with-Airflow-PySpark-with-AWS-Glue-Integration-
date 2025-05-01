FROM apache/airflow:2.6.0-python3.8
COPY scripts/ /opt/airflow/scripts/
RUN pip install --no-cache-dir -r /opt/airflow/scripts/requirements.txt
