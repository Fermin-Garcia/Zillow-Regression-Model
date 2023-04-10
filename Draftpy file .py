def add_county_state(df): 
    import pandas as pd
    import numpy as np
    import os 
    if os.path.exists('state_and_county_fips_master.csv') == True:
        fips = pd.read_csv('state_and_county_fips_master.csv')
    else: 
        url = 'https://raw.githubusercontent.com/kjhealy/fips-codes/master/state_and_county_fips_master.csv'
        fips = pd.read_csv(url)
        fips.to_csv('state_and_county_fips_master.csv')
    df = pd.merge(df,fips,on='fips')
    fips['county_state']= fips['name'] + ', ' + fips['state']
    drop_cols = ['name', 'state', 'fips']
    fips = fips.drop(columns= drop_cols)
    fips = fips.dropna()
    return df
    
    
def zillow_imports():
    import wrangle_zillow as w 
    import pandas as pd
    import seaborn as sns 
    import matplotlib.pyplot as plt 