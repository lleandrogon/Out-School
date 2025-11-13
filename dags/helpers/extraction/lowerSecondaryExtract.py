import pandas as pd
import pprint

def extract_lower_secondary(**kwargs):
    df = pd.read_csv("/opt/airflow/volumes/Lower Secondary.csv", encoding = "latin1")
    pprint.pprint(df)

    return df