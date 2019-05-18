## 1. Missing Values ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

cols = ['PID', 'Year Built', 'Year Remod/Add', 'Garage Yr Blt', 'Mo Sold', 'Yr Sold']

numerical_train = train.select_dtypes(['int', 'float']).copy()
numerical_train.drop(cols, inplace=True, axis=1)
print(numerical_train.head())

null_series = numerical_train.isnull().sum()
full_cols_series = null_series[null_series == 0]
print(full_cols_series)

## 2. Correlating Feature Columns With Target Column ##

train_subset = train[full_cols_series.index]
correlation_matrix = train_subset.corr()
sorted_corrs = correlation_matrix.abs().SalePrice.sort_values()
sorted_corrs

## 3. Correlation Matrix Heatmap ##

import matplotlib.pyplot as plt
import seaborn as sns

strong_corrs = sorted_corrs[sorted_corrs >= 0.3]
corrmat = train_subset[strong_corrs.index].corr()

sns.heatmap(corrmat)
plt.show()


## 4. Train And Test Model ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

## Final Dataframe Cols
final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])

## Features and Target
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'

train = train[final_corr_cols.index].dropna()
test = test[final_corr_cols.index].dropna()

## Fitting the model
lr = LinearRegression().fit(train[features], train[target])

## Making predictions
train_predictions = lr.predict(train[features])
test_predictions = lr.predict(test[features])

## Finding RMSE
train_mse = mean_squared_error(train_predictions, train[target])
train_rmse = np.sqrt(train_mse)

test_mse = mean_squared_error(test_predictions, test[target])
test_rmse = np.sqrt(test_mse)

print(train_rmse)
print(test_rmse)

## 5. Removing Low Variance Features ##

## Rescaling
unit_df = (train[features] - train[features].min())/(train[features].max() - train[features].min())
print(unit_df.head())

## Confirming that max and min are between 0-1
print("MAX")
print(unit_df.max())

print("\nMIN")
print(unit_df.min())

## Calculating variance of the columns and sorting them 
sorted_vars = unit_df.var().sort_values()
sorted_vars

## 6. Final Model ##

 ## Setting a cutoff variance of 0.15 and removing Open Porch SF
# Features and Target
features = features.drop('Open Porch SF')
target = 'SalePrice'

## Fitting the model
lr = LinearRegression().fit(train[features], train[target])

## Making predictions
train_predictions = lr.predict(train[features])
test_predictions = lr.predict(clean_test[features])

## Finding RMSE
train_mse_2 = mean_squared_error(train_predictions, train[target])
train_rmse_2 = np.sqrt(train_mse_2)

test_mse_2 = mean_squared_error(test_predictions, clean_test[target])
test_rmse_2 = np.sqrt(test_mse_2)

print(train_rmse_2)
print(test_rmse_2)