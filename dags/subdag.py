from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.subdag import SubDagOperator
from datetime import datetime

# Function to create a SubDAG
def subdag_example(parent_dag_name, child_dag_name, args):
    subdag = DAG(
        dag_id=f"{parent_dag_name}.{child_dag_name}",
        default_args=args,
        schedule_interval="@daily",
    )

    with subdag:
        task_1 = DummyOperator(task_id="task_1", dag=subdag)
        task_2 = DummyOperator(task_id="task_2", dag=subdag)
        task_3 = DummyOperator(task_id="task_3", dag=subdag)

        task_1 >> task_2 >> task_3

    return subdag

# Default arguments for the parent DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
}

# Define the parent DAG
parent_dag = DAG(
    dag_id="parent_dag",
    default_args=default_args,
    schedule_interval="@daily",
)

# Define tasks in the parent DAG
with parent_dag:
    start = DummyOperator(task_id="start")
    
    subdag_task = SubDagOperator(
        task_id="subdag_task",
        subdag=subdag_example("parent_dag", "subdag_task", default_args),
        dag=parent_dag,
    )
    
    end = DummyOperator(task_id="end")

    start >> subdag_task >> end
