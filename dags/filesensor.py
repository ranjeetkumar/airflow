from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.dummy import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 31),
    'retries': 1,
}

with DAG(dag_id='file_sensor_example',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    start = DummyOperator(task_id='start')

    wait_for_file = FileSensor(
        task_id='wait_for_file',
        filepath='files/file.txt',  # Change this to your file path
        fs_conn_id = 'fs_conn_id',
        poke_interval=5,  # Time (in seconds) between each check
        timeout=600  # Maximum time (in seconds) to wait for the file
    )

    end = DummyOperator(task_id='end')

    start >> wait_for_file >> end
