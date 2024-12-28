from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("chain_tasks", start_date=datetime(2024, 1, 1), schedule_interval="@daily") as dag:
    task1 = BashOperator(task_id="task1", bash_command="echo 'Task 1'")
    task2 = BashOperator(task_id="task2", bash_command="echo 'Task 2'")
    task3 = BashOperator(task_id="task3", bash_command="echo 'Task 3'")
    
    task1 >> task2 >> task3
