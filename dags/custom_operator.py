from airflow import DAG
from datetime import datetime
from my_custom_plugin import MyCustomOperator

with DAG(dag_id="my_custom_dag", start_date=datetime(2023, 1, 1)) as dag:
    task = MyCustomOperator(
        task_id="run_my_custom_operator",
        my_param="Hello, plugins!"
    )
