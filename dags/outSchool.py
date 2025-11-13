from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from datetime import datetime
import pendulum

from helpers.extraction.primaryExtract import *
from helpers.extraction.lowerSecondaryExtract import *
from helpers.extraction.upperSecondaryExtract import *

dag = DAG(
    dag_id = "out_school",
    schedule = "0 21 * * *",
    default_args = {
        "owner": "Airflow",
        "retries": 1,
        "start_date": pendulum.datetime(2025, 11, 1, tz = "America/Sao_Paulo")
    },
    catchup = False,
    tags = ["out", "school"]
)

e_primary = PythonOperator(
    task_id = "extract_primary",
    python_callable = extract_primary,
    dag = dag
)

e_lower_secondary = PythonOperator(
    task_id = "extract_lower_secondary",
    python_callable = extract_lower_secondary,
    dag = dag
)

e_upper_secondary = PythonOperator(
    task_id = "extract_upper_secondary",
    python_callable = extract_upper_secondary,
    dag = dag
)

e_primary

e_lower_secondary

e_upper_secondary