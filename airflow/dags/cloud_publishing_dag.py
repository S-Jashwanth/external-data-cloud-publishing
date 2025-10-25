from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.main import main as publish_main

with DAG('cloud_publishing', start_date=datetime(2025,1,1), schedule_interval='@daily', catchup=False) as dag:
    publish = PythonOperator(task_id='publish_data', python_callable=publish_main)
