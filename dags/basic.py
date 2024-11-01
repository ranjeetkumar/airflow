from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'catchup':False
}

def greet():
    print("Hello, Airflow!")

with DAG('sample_dag_with_retries', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    start = DummyOperator(task_id='start')
    greet_task = PythonOperator(task_id='greet', python_callable=greet)
    end = DummyOperator(task_id='end')

    start >> greet_task >> end
