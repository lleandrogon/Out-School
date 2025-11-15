from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd

def load_data(**kwargs):
    df_p, df_ls, df_us = kwargs["ti"] \
        .xcom_pull(task_ids = [
            "transform_primary",
            "transform_lower_secondary", 
            "transform_upper_secondary"
        ])
    
    hook = PostgresHook(
        postgres_conn_id = "education_docker",
        schema = "out_school"
    )

    df_combined = pd.concat([df_p, df_ls, df_us], ignore_index = True)
    df_combined = df_combined.astype(object).where(pd.notnull(df_combined), None)

    rows = df_combined.values.tolist()

    query = """--sql
        INSERT INTO out_school (
            iso3,
            countries_and_areas,
            region,
            sub_region,
            development_regions,
            total,
            female,
            male,
            rural_residence,
            urban_residence,
            poorest_wealth_quintile,
            second_wealth_quintile,
            middle_wealth_quintile,
            fourth_wealth_quintile,
            richest_wealth_quintile,
            data_source,
            time_period,
            education_level
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (countries_and_areas, data_source, time_period, education_level)
        DO NOTHING
    """

    rows = df_combined[
        [
            "iso3",
            "countries_and_areas",
            "region",
            "sub_region",
            "development_regions",
            "total",
            "female",
            "male",
            "rural_residence",
            "urban_residence",
            "poorest_wealth_quintile",
            "second_wealth_quintile",
            "middle_wealth_quintile",
            "fourth_wealth_quintile",
            "richest_wealth_quintile",
            "data_source",
            "time_period",
            "education_level"
        ]
    ].itertuples(index=False, name = None)

    for row in rows:
        hook.run(query, parameters=row)