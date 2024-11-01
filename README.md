# Airflow Project with Docker Compose

This repository sets up an Apache Airflow environment using Docker Compose. It includes steps to initialize the Airflow database, start up the services, create an admin user, and trigger DAGs via the Airflow REST API.

## Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup Instructions

### Step 1: Initialize the Airflow Database

Run the following command to initialize the Airflow database:
```bash
docker-compose run webserver airflow db init
```

### Step 2: Start the Airflow Services

Use Docker Compose to bring up the Airflow webserver and other related services in detached mode:
```bash
docker-compose up -d
```

### Step 3: Create an Admin User

After the services are running, create an admin user with the following command:
```bash
docker-compose run webserver airflow users create \
  --username admin \
  --firstname FIRST_NAME \
  --lastname LAST_NAME \
  --role Admin \
  --email your_email@example.com
```
- **Password:** The password for the `admin` user is set to `admin`.

### Step 4: Trigger a DAG Run via API

You can trigger a DAG using Airflow's REST API. Replace `file_sensor_example` with the name of your DAG and run the following `curl` command:
```bash
curl -X POST -u admin:admin http://localhost:8080/api/v1/dags/file_sensor_example/dagRuns \
  -H "Content-Type: application/json" \
  -d '{"conf": {"key": "value"}}'
```

- This command authenticates as the `admin` user and triggers a DAG run with a specified configuration.
- Replace `file_sensor_example` with your DAG ID and update `{"key": "value"}` with the actual configuration required.

### Accessing the Airflow UI

- Open your browser and navigate to [http://localhost:8080](http://localhost:8080) to access the Airflow web interface.
- Log in with the credentials:
  - **Username:** `admin`
  - **Password:** `admin`

## Troubleshooting

- If the services don't start as expected, check the Docker logs:
```bash
docker-compose logs
```

## Additional Information

- For more details on configuring Airflow with Docker, refer to the [Airflow Docker documentation](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).
- You can create additional users by following the [Airflow CLI documentation](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#cli-users).

---

Happy DAGging!

