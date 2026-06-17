from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner': 'kaviya',
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

@dag(
    dag_id='etl_template',
    start_date=datetime(2024, 6, 1),
    schedule=None,
    catchup=False,
    default_args=default_args
)
def etl_pipeline():

    @task
    def extract():
        print("Extracting data...")

    @task
    def transform():
        print("Transforming data...")

    @task
    def load():
        print("Loading data...")

    extract() >> transform() >> load()

etl_pipeline()