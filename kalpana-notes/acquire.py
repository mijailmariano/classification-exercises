import os
import pymysql
import pandas as pd
import env 
from env import user, password, host

def get_titanic_data():
    filename = "titatic.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=[0])
    else:
        db_url = f'mysql+pymysql://{user}:{password}@{host}/titanic_db'
        df = pd.read_sql("SELECT * FROM passengers", db_url)
        df.to_csv(filename)
        return df

def get_iris_data():
    # editing for "caching" exercise
    filename = "iris.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=[0])
    else:
        db_url = f'mysql+pymysql://{user}:{password}@{host}/iris_db'
        query = ''' 
        SELECT * 
        FROM measurements
        RIGHT JOIN species
        USING (species_id)
        '''
        df = pd.read_sql(query, db_url)
        df.to_csv(filename)
        return df

def get_telco_data():
    # editing for "caching" exercise
    filename = "telco.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=[0])
    else:
        db_url = f'mysql+pymysql://{user}:{password}@{host}/telco_churn'
        query = ''' 
        SELECT *
        FROM customers
        RIGHT JOIN contract_types using (contract_type_id)
        RIGHT JOIN payment_types using (payment_type_id)
        RIGHT JOIN internet_service_types using (internet_service_type_id)
        '''
        df = pd.read_sql(query, db_url)
        df.to_csv(filename)
        return df
