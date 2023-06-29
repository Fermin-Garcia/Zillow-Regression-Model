# Store all of the necessary functions to automate your process from acquiring the data to returning a cleaned dataframe with no missing values in your wrangle.py file. Name your final function wrangle_zillow.


import env
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import QuantileTransformer

import numpy as np
import os 


def aquire_zillow_data():
    query='\
    select bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt,     taxamount,fips\
    from properties_2017\
    left join propertylandusetype using(propertylandusetypeid)\
    where propertylandusedesc = "Single Family Residential"'
    
    if os.path.exists('zillow.csv') == True:
        return pd.read_csv('zillow.csv')
    else:
        df = pd.read_sql(query, get_connection())
        df.to_csv('zillow.csv')
        return pd.read_csv('zillow.csv')

    
def get_connection(user=env.user,password=env.password,host=env.host,database=env.database):
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'   

def add_county_state(df): 
  
    if os.path.exists('state_and_county_fips_master.csv') == True:
        fips = pd.read_csv('state_and_county_fips_master.csv')
    else: 
        url = 'https://raw.githubusercontent.com/kjhealy/fips-codes/master/state_and_county_fips_master.csv'
        fips = pd.read_csv(url)
        fips.to_csv('state_and_county_fips_master.csv')
    fips['county_state']= fips['name'] + ', ' + fips['state']
    df = pd.merge(df,fips,on='fips')
    df = df.drop(columns = ['Unnamed: 0','name','state', 'fips'])
    
    return df
    

# Function to prepare the data for modeling
def prepare(df):
    # Drop unnecessary columns and rows with missing values
    df = df.drop(columns='Unnamed: 0')
    df = df.dropna()
    
    # Rename columns for better readability
    cols_name = ['bedrooms', 'bathrooms', 'calculated_finished_squarefeet',
           'tax_valuedollar_cnt', 'year_built', 'tax_amount', 'fips']
    df.set_axis(cols_name, axis=1, inplace=True)
    df['year_built'] = df['year_built'].astype(int)
    
    # Handle Outliers:
    # The general rule for outliers are:
    ## Upper bond: Q3 + 1.5*IQR
    ## Lower bund: Q1 - 1.5*IQR
    # Bonds are manually adjusted for each feature
    df = df[df.bedrooms <= 6]
    df = df[df.bedrooms >= 1]

    df = df[df.bathrooms <= 6.5]
    df = df[df.bathrooms >= 0.5]

    df = df[df.calculated_finished_squarefeet <= 4800]
    df = df[df.calculated_finished_squarefeet >= 500]
    
    # Add county and state columns to the data
    df = add_county_state(df)
    
    # gets dummy values for object columns:
    df = pd.get_dummies(df, columns = ['county_state'])
    
    # Cleans up the columns name to easier to process names.
    df.rename(columns = {
    'county_state_Los Angeles County, CA' : 'la_county_ca',
    'county_state_Orange County, CA' : 'orange_county_ca',
    'county_state_Ventura County, CA': 'ventura_county_ca'
    }, 
             inplace=True)
    cols = list(df.columns)
    cols.append(cols.pop(cols.index('tax_valuedollar_cnt')))
    df = df[cols]

    # Return the cleaned and preprocessed data
    return df

# Function to split the data into training, validation, and testing sets
def split(df):
    '''
    This function splits a dataframe into 
    train, validate, and test in order to explore the data and to create and validate models. 
    It takes in a dataframe and contains an integer for setting a seed for replication. 
    Test is 20% of the original dataset. The remaining 80% of the dataset is 
    divided between valiidate and train, with validate being .30*.80= 24% of 
    the original dataset, and train being .70*.80= 56% of the original dataset. 
    The function returns, train, validate and test dataframes. 
    '''
    df = df.sample(40000)
    train, test = train_test_split(df, test_size = .2, random_state=123)   
    train, validate = train_test_split(train, test_size=.3, random_state=123)
    
    return train, validate, test

from sklearn.preprocessing import QuantileTransformer

def apply_quantile_scaler(X_train, X_validate, X_test):
    """
    Applies quantile scaling on the input data
    
    Args:
    X_train: Training data features
    X_validate: Validation data features
    X_test: Test data features
    
    Returns:
    Transformed features for training, validation and test sets
    """
    # create scaler object
    scaler = QuantileTransformer(output_distribution='normal')
    
    # fit and transform the training data
    X_train_scaled = scaler.fit_transform(X_train)
    
    # transform the validation and test data using the trained scaler
    X_validate_scaled = scaler.transform(X_validate)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_validate_scaled, X_test_scaled

    
# Function to remove outliers from the data
def remove_outliers(df):   
    # Iterate through each column in the data
    col_list = list(df.columns)
    for col in col_list:
        # Get the quartiles for the column
        q1, q3 = df[col].quantile([.25, .75])  
        
        # Calculate the interquartile range (IQR)
        iqr = q3 - q1
        
        # Calculate the upper and lower bounds for outliers
        upper_bound = q3 + 1.5 * iqr   
        lower_bound = q1 - 1.5 * iqr   
        
        # Remove outliers from the column and update the data
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    # Return the data without outliers
    return df

# Function to identify the types of columns in the data
def find_column_types(df):
    # Initialize lists to store the names of continuous and categorical columns
    continous_vars = []
    categorical_vars = []
    
    # Iterate through each column in the data
    for cols in train.columns:
        # If the column contains object type data, it is categorical
        if train[cols].dtype == 'O':
           categorical_vars.append(cols)
        # Otherwise, it is continuous
        else:
            continous_vars.append(cols)
            
    # Return the names of the categorical and continuous columns
    return categorical_vars, continous_vars


from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler




def scale_and_plot_data(x_train, y_train, x_validate, y_validate, x_test, scaler=MinMaxScaler()):
    # scale the data
    scaler.fit(x_train)
    x_train_scaled = scaler.transform(x_train)
    x_validate_scaled = scaler.transform(x_validate)
    x_test_scaled = scaler.transform(x_test)

    # calculate the difference between the original and scaled data
    diff_train = x_train - x_train_scaled
    diff_validate = x_validate - x_validate_scaled
    diff_test = x_test - x_test_scaled

    # plot the difference
    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(10,15))
    axs[0,0].set_title('Training Data - Original')
    axs[0,0].boxplot(x_train)
    axs[0,1].set_title('Training Data - Scaled')
    axs[0,1].boxplot(x_train_scaled)
    axs[1,0].set_title('Validation Data - Original')
    axs[1,0].boxplot(x_validate)
    axs[1,1].set_title('Validation Data - Scaled')
    axs[1,1].boxplot(x_validate_scaled)
    axs[2,0].set_title('Test Data - Original')
    axs[2,0].boxplot(x_test)
    axs[2,1].set_title('Test Data - Scaled')
    axs[2,1].boxplot(x_test_scaled)
    fig.suptitle('Difference between Original and Scaled Data')
    plt.show()


def hypothesis_test(data, x, y, alpha=0.05):
    # Perform Pearson correlation test
    r, p = stats.pearsonr(data[x], data[y])
    print(f"The Pearson correlation coefficient between {x} and {y} is {r:.2f} with a p-value of {p:.2f}")

    # Determine whether to accept or reject null hypothesis
    if p < alpha:
        print(f"Since the p-value is less than {alpha}, we can reject the null hypothesis and conclude that {x} and {y}           are correlated.")
        print('_______________________________________________________')
    else:
        print(f"Since the p-value is greater than or equal to {alpha}, we fail to reject the null hypothesis and conclude         that there is insufficient evidence to suggest a correlation between {x} and {y}.")
        print('_______________________________________________________')



    ## Work in progress use at your own risk.\
