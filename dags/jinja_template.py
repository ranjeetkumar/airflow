from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG(
    'templating_dag',
    default_args={'start_date': datetime(2024, 10, 31)},
    schedule_interval='@daily',
)

bash_task = BashOperator(
    task_id='print_date',
    bash_command='echo "Today is {{ ds }}"',
    dag=dag,
)
