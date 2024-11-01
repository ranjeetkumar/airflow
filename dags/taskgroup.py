from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
}

# Create the main DAG
with DAG(
    dag_id='task_group_example',
    default_args=default_args,
    schedule_interval='@daily',
) as dag:

    start = DummyOperator(task_id='start')

    # Define Task Group for ETL Process
    with TaskGroup("etl_process") as etl_group:
        extract = DummyOperator(task_id='extract')
        transform = DummyOperator(task_id='transform')
        load = DummyOperator(task_id='load')

        extract >> transform >> load

    # Define Task Group for Reporting
    with TaskGroup("reporting_process") as reporting_group:
        generate_report = DummyOperator(task_id='generate_report')
        send_report = DummyOperator(task_id='send_report')

        generate_report >> send_report

    end = DummyOperator(task_id='end')

    # Define the task dependencies
    start >> etl_group >> reporting_group >> end
