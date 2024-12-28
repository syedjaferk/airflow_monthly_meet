from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    return {"name": "Airflow", "type": "ETL"}

def transform(ti):
    data = ti.xcom_pull(task_ids="extract")
    data["type"] = data["type"].upper()
    return data

def load(ti):
    data = ti.xcom_pull(task_ids="transform")
    print(f"Loaded data: {data}")

with DAG("simple_etl_pipeline", start_date=datetime(2024, 1, 1), schedule_interval="@daily") as dag:
    extract_task = PythonOperator(task_id="extract", python_callable=extract)
    transform_task = PythonOperator(task_id="transform", python_callable=transform)
    load_task = PythonOperator(task_id="load", python_callable=load)

    extract_task >> transform_task >> load_task
