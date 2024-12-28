from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(response.json())

with DAG("fetch_api_data", start_date=datetime(2024, 1, 1), schedule_interval="@daily") as dag:
    task = PythonOperator(task_id="fetch_data", python_callable=fetch_data)
