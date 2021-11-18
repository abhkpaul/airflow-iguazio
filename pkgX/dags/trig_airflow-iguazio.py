import sys
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

sys.path.insert(0, '/pkgX/dist/airflow_iguazio-1.0-py3.8.egg')
import pkgX.triggerFile

default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(dag_id='dag_airflow-iguazio',
         start_date=datetime(2021, 11, 18),
         max_active_runs=3,
         schedule_interval='@daily',
         default_args=default_args,
         catchup=False
         ) as dag:

    triggerDAG = PythonOperator(task_id="triggerDAG",
                                  python_callable=pkgX.triggerFile.triggerRuns())