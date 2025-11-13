import pandas as pd
import pprint

def extract_upper_secondary(**kwargs):
    df = pd.read_csv("/opt/airflow/volumes/Upper Secondary.csv", encoding = "latin1")
    pprint.pprint(df)

    return df