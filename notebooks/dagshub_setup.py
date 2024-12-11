import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/ussmanabbasi001/Mlflow.mlflow')
dagshub.init(repo_owner='ussmanabbasi001', repo_name='Mlflow', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)