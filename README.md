# Project goals:
    - Construct an ML Regression model that predict propery tax assessed values ('taxvaluedollarcnt') of Single Family Properties using attributes of the properties.

    - Find the key drivers of property value for single family properties. Some questions that come to mind are:
           Why do some properties have a much higher value than others when they are located so        close to each other Why are some properties valued so differently from others when          they have nearly the same physical attributes but only differ in location 
           Is having 1 bathroom worse than having 2 bedrooms?

    - Deliver a report that the data science team can read through and replicate, understand what steps were taken, why and what the outcome was.

    - Make recommendations on what works or doesn't work in prediction these homes' values.



## Project description: 
    A zillow ML model that will 

## Project planning (lay out your process through the data science pipeline)
    planning: While here we decieded what was the features we wanted to explore. We planed on how we would potientally approach the data and handle potiental issues with data
    prepare:
    - The wrangle.py file provides a set of functions that aim to automate the process of acquiring, cleaning, and preparing data for a Zillow project. The final function of this file is     wrangle_zillow(), which returns a cleaned dataframe with no missing values.

    - The aquire_zillow_data() function acquires the necessary data from the Zillow database or the local CSV file if it exists. 
    The data is filtered to include only single-family residential, properties and specific columns.

    - The get_connection() function creates a connection string to the Zillow database using environment variables.

    - The add_county_state() function retrieves and merges the county and state data to the original dataset based on fips code.

    - The remove_outliers() function removes outliers in the data based on interquartile ranges.

    - The prepare() function prepares the data for modeling by dropping unnecessary columns, renaming columns, removing missing values, 
    removing outliers, adding county and state columns, getting dummy variables for the categorical 
    columns, and finally ordering the columns.

    - The split_data() function splits the data into training, validation, and testing sets.

    - The quantile_scaler() function scales the data using Quantile Transformer to normalize the data and preserve the distribution.

    - The find_column_types() function finds the types of columns in the data, which are categorical or continuous.





## Key findings, recommendations, and takeaways from your project.

    Collect more data on the areal events

    Collect more data on demographics (i.g income, material status, education, career type )

    Develop machine learning models with higher accuracy (lower RMSE) with the prosed data and make better predictions.

    Continue to collect on future data ,so we can help our model better predict the tax value dollar cnt or 'Sale Price'


# Sources:
    - For county and state 
        https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt
    - Fips Code 
        git@github.com:kjhealy/fips-codes.git