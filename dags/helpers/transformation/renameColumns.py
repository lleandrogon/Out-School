import pandas as pd

def rename_columns(df):
    rename_cols = {
        "ISO3": "iso3",
        "Countries and areas": "countries_and_areas",
        "Region": "region",
        "Sub-region": "sub_region",
        "Development Regions": "development_regions",
        "Total": "total",
        "Female": "female",
        "Male": "male",
        "Rural_Residence": "rural_residence",
        "Urban_Residence": "urban_residence",
        "Poorest_Wealth quintile": "poorest_wealth_quintile",
        "Second_Wealth quintile": "second_wealth_quintile",
        "Middle_Wealth quintile": "middle_wealth_quintile",
        "Fourth_Wealth quintile": "fourth_wealth_quintile",
        "Richest_Wealth quintile": "richest_wealth_quintile",
        "Data source": "data_source",
        "Time period": "time_period"
    }

    df.rename(columns = rename_cols, inplace = True)

    return df