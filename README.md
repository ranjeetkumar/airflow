docker-compose run webserver airflow db init
docker-compose up -d
docker-compose run webserver airflow users create \
   --username admin \
   --firstname FIRST_NAME \
   --lastname LAST_NAME \
   --role Admin \
   --email your_email@example.com


#password: admin
curl -X POST \
  -u admin:admin \
  http://localhost:8080/api/v1/dags/file_sensor_example/dagRuns \
  -H "Content-Type: application/json" \
  -d '{"conf": {"key": "value"}}'

