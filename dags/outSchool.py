from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

from datetime import datetime
import pendulum

from helpers.extraction.primaryExtract import *
from helpers.extraction.lowerSecondaryExtract import *
from helpers.extraction.upperSecondaryExtract import *
from helpers.transformation.primaryTransform import *
from helpers.transformation.lowerSecondaryTransform import *
from helpers.transformation.upperSecondaryTransform import *
from helpers.queries.createTableOutSchool import *

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

e_validate = BashOperator(
    task_id = "extract_validate",
    bash_command = "echo 'Extração validada!'"
)

t_primary = PythonOperator(
    task_id = "transform_primary",
    python_callable = transform_primary,
    dag = dag
)

t_lower_secondary = PythonOperator(
    task_id = "transform_lower_secondary",
    python_callable = transform_lower_secondary,
    dag = dag
)

t_upper_secondary = PythonOperator(
    task_id = "transform_upper_secondary",
    python_callable = transform_upper_secondary,
    dag = dag
)

t_validate = BashOperator(
    task_id = "transform_validate",
    bash_command = "echo 'Transformação validada!'"
)

ct_out_school = SQLExecuteQueryOperator(
    task_id = "create_table_out_school",
    conn_id = "education_docker",
    sql = create_table,
    dag = dag
)

[e_primary, e_lower_secondary, e_upper_secondary] \
    >> e_validate \
    >> [t_primary, t_lower_secondary, t_upper_secondary] \
    >> t_validate \
    >> ct_out_school