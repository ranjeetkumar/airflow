from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 31),
}

with DAG('triggering_dag',
         schedule_interval='@once',
         default_args=default_args,
         catchup=False) as dag:

    start_task = DummyOperator(task_id='start')

    trigger_next_dag = TriggerDagRunOperator(
        task_id='trigger_next_dag',
        trigger_dag_id='target_dag',  # Name of the DAG to trigger
        conf={'key': 'value'},  # Optional parameters to pass to the triggered DAG
        wait_for_completion=True  # Wait for the triggered DAG to complete
    )

    end_task = DummyOperator(task_id='end')

    start_task >> trigger_next_dag >> end_task
