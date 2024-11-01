from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_number(number):
    print(f"Number: {number}")

dag = DAG(
    'dynamic_dag',
    default_args={'start_date': datetime(2024, 10, 31)},
    schedule_interval='@daily',
    catchup=False
)

# Dynamically create tasks
for i in range(5):
    task = PythonOperator(
        task_id=f'print_number_{i}',
        python_callable=print_number,
        op_kwargs={'number': i},
        dag=dag,
    )
