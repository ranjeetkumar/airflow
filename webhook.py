from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/trigger_dag', methods=['POST'])
def trigger_dag():
    # Airflow REST API URL to trigger the DAG
    dag_run_url = 'http://localhost:8080/api/v1/dags/file_sensor_example/dagRuns'
    response = requests.post(dag_run_url, json={'conf': request.json})
    return response.json(), response.status_code

if __name__ == '__main__':
    app.run(port=5000)

