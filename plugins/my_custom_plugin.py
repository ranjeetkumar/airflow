# my_custom_plugin.py

from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

# Define the custom operator
class MyCustomOperator(BaseOperator):
    @apply_defaults
    def __init__(self, my_param, *args, **kwargs):
        super(MyCustomOperator, self).__init__(*args, **kwargs)
        self.my_param = my_param

    def execute(self, context):
        print(f"Running MyCustomOperator with param: {self.my_param}")

# Define the plugin
class MyPlugin(AirflowPlugin):
    name = "my_plugin"
    operators = [MyCustomOperator]
