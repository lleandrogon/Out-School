create_table = """--sql
    CREATE TABLE IF NOT EXISTS out_school(
        id SERIAL PRIMARY KEY,
        iso3 VARCHAR(3),
        countries_and_areas VARCHAR(100),
        region VARCHAR(50),
        sub_region VARCHAR(50),
        development_regions VARCHAR(100),
        total DECIMAL(5,2),
        female DECIMAL(5,2),
        male DECIMAL(5,2),
        rural_residence DECIMAL(5,2),
        urban_residence DECIMAL(5,2),
        poorest_wealth_quintile DECIMAL(5,2),
        second_wealth_quintile DECIMAL(5,2),
        middle_wealth_quintile DECIMAL(5,2),
        fourth_wealth_quintile DECIMAL(5,2),
        richest_wealth_quintile DECIMAL(5,2),
        data_source VARCHAR(100),
        time_period INT,
        education_level VARCHAR(20),
        CONSTRAINT country_time_source UNIQUE (countries_and_areas, data_source, time_period, education_level)
    );
"""