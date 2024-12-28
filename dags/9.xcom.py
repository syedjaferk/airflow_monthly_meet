from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def push_data(ti):
    ti.xcom_push(key="sample_key", value="Hello from XCom!")

def pull_data(ti):
    value = ti.xcom_pull(key="sample_key", task_ids="push_data")
    print(f"Received value: {value}")

with DAG("xcom_example", start_date=datetime(2024, 1, 1), schedule_interval="@daily") as dag:
    push = PythonOperator(task_id="push_data", python_callable=push_data)
    pull = PythonOperator(task_id="pull_data", python_callable=pull_data)

    push >> pull
