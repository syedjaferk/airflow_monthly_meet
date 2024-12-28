from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("hello_world", start_date=datetime(2024, 1, 1), schedule_interval="@daily") as dag:
    task = BashOperator(task_id="print_hello", bash_command="echo 'Hello, World!'")
