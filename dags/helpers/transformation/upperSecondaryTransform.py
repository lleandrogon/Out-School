import pandas as pd

def transform_upper_secondary(**kwargs):
    df = kwargs["ti"].xcom_pull(task_ids = "extract_upper_secondary")

    df["Countries and areas"] = df["Countries and areas"].replace({
        "Bolivia (Plurinational State of)": "Bolivia",
        "Iran (Islamic Republic of)": "Iran",
        "Micronesia (Federated States of)": "Micronesia",
        "Venezuela (Bolivarian Republic of)": "Venezuela"
    })

    df.dropna(inplace = True, subset = ["Region"])

    df.dropna(inplace = True, subset = ["Total"])

    return df