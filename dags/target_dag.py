from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG('target_dag',
         schedule_interval=None,  # This DAG is triggered externally
         default_args=default_args,
         catchup=False) as dag:

    start_task = DummyOperator(task_id='start')
    end_task = DummyOperator(task_id='end')

    start_task >> end_task
