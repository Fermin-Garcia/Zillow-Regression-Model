# Zillow Single-Family Home Value Prediction

By Fermin F. Garcia IV

## Overview

This project builds a regression model to predict the property tax assessed value (`taxvaluedollarcnt`) of single-family homes from Zillow's 2017 property data. It also looks for the features that drive home value the most.

The work was completed as part of the Codeup Data Science program, with a short presentation of the findings written for Zillow's data science team.

## Goals

- Build a regression model that predicts assessed home value from property attributes.
- Identify the main drivers of home value.
- Recommend next steps for improving the model.

## Data

- **Source:** Codeup's copy of the Zillow database (`properties_2017` joined to `propertylandusetype`).
- **Filter:** properties classified as "Single Family Residential".
- **Counties:** Los Angeles, Orange, and Ventura (California), derived from FIPS codes.
- **Sample:** 40,000 rows, split 56% train / 24% validate / 20% test (22,400 training rows).

### Data Dictionary

| Feature | Description |
| --- | --- |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms (half baths count as 0.5) |
| `calculated_finished_squarefeet` | Finished living area in square feet |
| `year_built` | Year the home was built |
| `tax_amount` | Property tax billed for the 2017 assessment year |
| `la_county_ca`, `orange_county_ca`, `ventura_county_ca` | One-hot encoded county |
| `tax_valuedollar_cnt` | **Target:** tax assessed value of the property, in dollars |

## Preparation

- Dropped rows with missing values.
- Removed outliers with bounds set per feature: 1 to 6 bedrooms, 0.5 to 6.5 bathrooms, and 500 to 4,800 square feet.
- Mapped FIPS codes to county names and one-hot encoded them.
- Scaled features with `MinMaxScaler` before modeling.

## Exploration

- A correlation heat map showed `calculated_finished_squarefeet`, `bathrooms`, and `tax_amount` had the strongest relationships with assessed value.
- Bathroom count was tested for correlation with assessed value (H<sub>0</sub>: no correlation; H<sub>a</sub>: correlation exists).

## Modeling Results

Models were compared by root mean squared error (RMSE). The baseline predicts the mean assessed value of the training set for every home.

| Model | RMSE |
| --- | --- |
| Baseline (mean) | ~$430,000 |
| Linear Regression (OLS) | ~$75,700 |
| LassoLars | ~$75,700 |

Ordinary least squares linear regression performed best by a small margin and cut prediction error by about 82% compared to the baseline.

## Limitations

`tax_amount` is calculated from the assessed value, so including it as a feature leaks information about the target and makes the model look better than it would on homes without a tax bill. The next version should drop `tax_amount` and rely on physical and location features only.

## Next Steps

- Remove `tax_amount` and retrain to measure performance using only property features.
- Add location detail beyond county (zip code, latitude/longitude, lot size).
- Add neighborhood-level demographic data such as income and education.
- Try nonlinear models such as random forests or gradient boosting.

## How to Reproduce

1. Clone this repository.
2. Create an `env.py` file with `user`, `password`, `host`, and `database` values for a MySQL server that has the Zillow database. Do not commit this file; it is already listed in `.gitignore`.
3. Install the requirements: `pandas`, `numpy`, `scikit-learn`, `scipy`, `matplotlib`, `seaborn`, and `pymysql`.
4. Run `final_presentation.ipynb` from top to bottom. It uses the functions in `wrangle.py` to acquire, prepare, and split the data.

## Files

| File | Purpose |
| --- | --- |
| `final_presentation.ipynb` | Final report and presentation notebook |
| `wrangle.py` | Acquire, prepare, and split functions used by the final notebook |
| `acquire.py`, `prepare.py`, `explore.py`, `modeling.py` | Stage-by-stage modules |
| `acquire.ipynb`, `prepare.ipynb`, `explore.ipynb`, `modeling.ipynb` | Working notebooks for each stage |
