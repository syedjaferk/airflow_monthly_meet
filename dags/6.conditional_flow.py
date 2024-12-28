from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

def decide_branch():
    return "branch_1" if datetime.now().minute % 2 == 0 else "branch_2"

with DAG("conditional_workflow", start_date=datetime(2024, 1, 1), schedule_interval="@daily") as dag:
    start = DummyOperator(task_id="start")
    branch = BranchPythonOperator(task_id="branch", python_callable=decide_branch)
    branch_1 = DummyOperator(task_id="branch_1")
    branch_2 = DummyOperator(task_id="branch_2")
    end = DummyOperator(task_id="end")

    start >> branch >> [branch_1, branch_2] >> end
