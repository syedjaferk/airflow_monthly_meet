from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("dynamic_tasks", start_date=datetime(2024, 1, 1), schedule_interval="@daily") as dag:
    for i in range(5):
        BashOperator(
            task_id=f"dynamic_task_{i}",
            bash_command=f"echo 'This is task {i}'"
        )
