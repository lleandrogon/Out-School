import pandas as pd
import pprint

def extract_primary(**kwargs):
    df = pd.read_csv("/opt/airflow/volumes/Primary.csv", encoding = "latin1")
    pprint.pprint(df)

    return df