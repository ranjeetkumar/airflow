from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 31),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'my_first_dag',
    default_args=default_args,
    description='A simple first DAG',
    schedule_interval='* * * * *',  # Run once a day
)
def my_task_function():
    print("Hello, Airflow!")
# Define tasks
start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)
task1 = PythonOperator(
    task_id='task1',
    python_callable=my_task_function,
    dag=dag,
)
# Set task dependencies
start >> end >> task1









