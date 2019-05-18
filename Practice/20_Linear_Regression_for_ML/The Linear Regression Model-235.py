## 2. Introduction To The Data ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', '\t')
train = data[:1460]
test = data[1460:]
print(train.info())
print(test.info())

target = 'SalePrice'




## 3. Simple Linear Regression ##

import matplotlib.pyplot as plt
# For prettier plots.
import seaborn as sns

fig = plt.figure(figsize=(7,15))

ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)


train.plot("Garage Area", "SalePrice", ax = ax1, kind="scatter")
train.plot("Gr Liv Area", "SalePrice", ax = ax2, kind="scatter")
train.plot("Overall Cond", "SalePrice", ax = ax3, kind="scatter")

plt.show()

## 5. Using Scikit-Learn To Train And Predict ##

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(train[['Gr Liv Area']], train['SalePrice'])
a1 = lr.coef_
a0 = lr.intercept_

## 6. Making Predictions ##

import numpy as np
from sklearn.metrics import mean_squared_error

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])

train_predictions = lr.predict(train[['Gr Liv Area']])
test_predictions = lr.predict(test[['Gr Liv Area']])

train_mse = mean_squared_error(train_predictions, train['SalePrice'])
train_rmse = np.sqrt(train_mse)

test_mse = mean_squared_error(test_predictions, test['SalePrice'])
test_rmse = np.sqrt(test_mse)


## 7. Multiple Linear Regression ##

## Features and Target
features = ['Overall Cond', 'Gr Liv Area']
target = ['SalePrice']

train_features = train[features]
test_features = test[features]

train_target = train[target]
test_target = test[target]

## Fitting the model
lr = LinearRegression().fit(train_features, train_target)

## Making Predictions
train_predictions = lr.predict(train_features)
test_predictions = lr.predict(test_features)

## Findig Root Mean Squared Error
train_mse_2 = mean_squared_error(train_predictions, train_target)
train_rmse_2 = np.sqrt(train_mse)

test_mse_2 = mean_squared_error(test_predictions, test_target)
test_rmse_2 = np.sqrt(test_mse)

print(train_rmse_2)
print(test_rmse_2)