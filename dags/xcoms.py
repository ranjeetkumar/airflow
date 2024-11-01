from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def push_function(**kwargs):
    value = "Hello from push_function"
    kwargs['ti'].xcom_push(key='my_key', value=value)

def pull_function(**kwargs):
    value = kwargs['ti'].xcom_pull(task_ids='push_task', key='my_key')
    print(f"Pulled value: {value}")

dag = DAG(
    'xcom_dag',
    default_args={'start_date': datetime(2024, 10, 31)},
    schedule_interval='@daily',
    catchup = False
)

push_task = PythonOperator(
    task_id='push_task',
    python_callable=push_function,
    provide_context=True,
    dag=dag,
)

pull_task = PythonOperator(
    task_id='pull_task',
    python_callable=pull_function,
    provide_context=True,
    dag=dag,
)

push_task >> pull_task
