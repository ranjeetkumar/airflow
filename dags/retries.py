from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def failing_task():
    raise Exception("Task failed!")

dag = DAG(
    'retry_dag',
    default_args={'start_date': datetime(2024, 10, 31), 'retries': 3, 'retry_delay': timedelta(minutes=5)},
    schedule_interval='@daily',
)

task = PythonOperator(
    task_id='failing_task',
    python_callable=failing_task,
    dag=dag,
)
