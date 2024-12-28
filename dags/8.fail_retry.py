from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG("fail_and_retry", start_date=datetime(2024, 1, 1), schedule_interval="@daily") as dag:
    task = BashOperator(
        task_id="fail_task",
        bash_command="exit 1",
        retries=3,
        retry_delay=timedelta(seconds=30)
    )
