import pandas as pd

from .renameColumns import *

def transform_lower_secondary(**kwargs):
    df = kwargs["ti"].xcom_pull(task_ids = "extract_lower_secondary")

    df["Countries and areas"] = df["Countries and areas"].replace({
        "Bolivia (Plurinational State of)": "Bolivia",
        "Iran (Islamic Republic of)": "Iran",
        "Micronesia (Federated States of)": "Micronesia",
        "Venezuela (Bolivarian Republic of)": "Venezuela"
    })

    df.dropna(inplace = True, subset = ["Region"])

    df.dropna(inplace = True, subset = ["Total"])

    rename_columns(df)

    df["education_level"] = "lower_secondary"

    return df