import env
import os
import pandas as pd


def acquire_zillow_data():
    """
    Acquires Zillow data by querying the database and saving the result in a CSV file.
    If the CSV file already exists, it returns the data from the file instead of querying the database again.
    
    Returns:
        DataFrame: Zillow data
        
    """
    query = "\
    select bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips \
    from properties_2017 \
    left join propertylandusetype using(propertylandusetypeid) \
    where propertylandusedesc = 'Single Family Residential'"

    if os.path.exists('zillow.csv'):
        # If the CSV file already exists, read the data from the file
        return pd.read_csv('zillow.csv')
    else:
        # Query the database, save the result in a CSV file, and return the data
        df = pd.read_sql(query, get_connection())
        df.to_csv('zillow.csv')
        return pd.read_csv('zillow.csv', index_col=0)


def get_connection(user=env.user, password=env.password, host=env.host, database=env.database):
    """
    Creates a connection string for MySQL using the provided credentials and database information.

    Args:
        user (str): MySQL username
        password (str): MySQL password
        host (str): MySQL host
        database (str): MySQL database name

    Returns:
        str: MySQL connection string

    """
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'
