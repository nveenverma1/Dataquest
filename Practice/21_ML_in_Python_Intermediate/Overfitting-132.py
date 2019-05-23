## 1. Introduction ##

import pandas as pd
columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("auto-mpg.data", delim_whitespace=True, names=columns)
filtered_cars = cars[cars['horsepower'] != '?'].copy()
filtered_cars['horsepower'] = filtered_cars['horsepower'].astype('float')

## 3. Bias-variance tradeoff ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

def train_and_test(cols):
    X = filtered_cars[[cols]]
    y = filtered_cars['mpg']
    
    m = LinearRegression().fit(X, y)
    predictions = m.predict(X)
    
    variance = predictions.var()
    mse = mean_squared_error(predictions, y)
    
    return (mse, variance)

cyl_mse, cyl_var = train_and_test('cylinders')
weight_mse, weight_var = train_and_test('weight')

## 4. Multivariate models ##

# Our implementation for train_and_test, takes in a list of strings.
def train_and_test(cols):
    # Split into features & target.
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    # Fit model.
    lr = LinearRegression()
    lr.fit(features, target)
    # Make predictions on training set.
    predictions = lr.predict(features)
    # Compute MSE and Variance.
    mse = mean_squared_error(filtered_cars["mpg"], predictions)
    variance = np.var(predictions)
    return(mse, variance)
cols = ['cylinders', 'displacement', 'horsepower','weight', 'acceleration', 'model year', 'origin']

one_mse, one_var = train_and_test(cols[:1])
print(one_mse, one_var)

two_mse, two_var = train_and_test(cols[:2])
print(two_mse, two_var)

three_mse, three_var = train_and_test(cols[:3])
print(three_mse, three_var)

four_mse, four_var = train_and_test(cols[:4])
print(four_mse, four_var)

five_mse, five_var = train_and_test(cols[:5])
print(five_mse, five_var)

six_mse, six_var = train_and_test(cols[:6])
print(six_mse, six_var)

seven_mse, seven_var = train_and_test(cols[:7])
print(seven_mse, seven_var)

## 5. Cross validation ##

from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import numpy as np

# Our implementation for train_and_test, takes in a list of strings.
def train_and_cross_val(cols):
    # Split into features & target.
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    # Fit model.
    kf = KFold(10, shuffle=True, random_state=3)
    
    variance_values = []
    mse_values = []
    
    for train_index, test_index in kf.split(features):
        X_train, X_test = features.iloc[train_index], features.iloc[test_index]
        y_train, y_test = target.iloc[train_index], target.iloc[test_index]
        
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        
        # Make predictions on training set.
        predictions = lr.predict(X_test)
        # Compute MSE and Variance.
        mse = mean_squared_error(y_test, predictions)
        mse_values.append(mse)
        
        variance = np.var(predictions)
        variance_values.append(variance)
    
    return(np.mean(mse_values), np.mean(variance_values))

cols = ['cylinders', 'displacement', 'horsepower','weight', 'acceleration', 'model year', 'origin']


two_mse, two_var = train_and_cross_val(cols[:2])
print(two_mse, two_var)

three_mse, three_var = train_and_cross_val(cols[:3])
print(three_mse, three_var)

four_mse, four_var = train_and_cross_val(cols[:4])
print(four_mse, four_var)

five_mse, five_var = train_and_cross_val(cols[:5])
print(five_mse, five_var)

six_mse, six_var = train_and_cross_val(cols[:6])
print(six_mse, six_var)

seven_mse, seven_var = train_and_cross_val(cols[:7])
print(seven_mse, seven_var)

## 6. Plotting cross-validation error vs. cross-validation variance ##

# # We've hidden the `train_and_cross_val` function to save space but you can still call the function!
# import matplotlib.pyplot as plt
        
# two_mse, two_var = train_and_cross_val(["cylinders", "displacement"])
# three_mse, three_var = train_and_cross_val(["cylinders", "displacement", "horsepower"])
# four_mse, four_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight"])
# five_mse, five_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
# six_mse, six_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
# seven_mse, seven_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration","model year", "origin"])

# fig, axes = fig.subplots(6, 2)
cols = ['cylinders', 'displacement', 'horsepower','weight', 'acceleration', 'model year', 'origin']

feature_num = []
mse_num = []
var_num = []

for i in range(2, 8):
    mse, var = train_and_cross_val(cols[:i])
    feature_num.append(i)
    mse_num.append(mse)
    var_num.append(var)

# plt.scatter(feature_num, mse_num, c='red', label='MSE')
# plt.scatter(feature_num, var_num, c='blue', label='Variance')
plt.scatter(feature_num, mse_num, c='red')
plt.scatter(feature_num, var_num, c='blue')
# plt.xlabel('No. of features')
plt.legend()
plt.show()