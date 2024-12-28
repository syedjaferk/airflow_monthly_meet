from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def greet():
    print("Hello from Python!")

with DAG("python_function", start_date=datetime(2024, 1, 1), schedule_interval="@daily") as dag:
    task = PythonOperator(task_id="greet", python_callable=greet)
