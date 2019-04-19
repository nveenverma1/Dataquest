## 1. Recap ##

import pandas as pd

train_df = pd.read_csv('dc_airbnb_train.csv')
test_df = pd.read_csv('dc_airbnb_test.csv')

## 2. Hyperparameter optimization ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params = [1, 2, 3, 4, 5]
mse_values = []
features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']

train_features = train_df[features]
train_target = train_df['price']

test_features = test_df[features]
test_target = test_df['price']

for i in hyper_params:
    knn = KNeighborsRegressor(algorithm='brute', n_neighbors=i)
    knn.fit(train_features, train_target)
    predictions = knn.predict(test_features)
    
    mse = mean_squared_error(test_target, predictions)
    mse_values.append(mse)

mse_values

## 3. Expanding grid search ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params = list(range(1, 21))
mse_values = []
features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']

train_features = train_df[features]
train_target = train_df['price']

test_features = test_df[features]
test_target = test_df['price']

for i in hyper_params:
    knn = KNeighborsRegressor(algorithm='brute', n_neighbors=i)
    knn.fit(train_features, train_target)
    predictions = knn.predict(test_features)
    
    mse = mean_squared_error(test_target, predictions)
    mse_values.append(mse)

mse_values

## 4. Visualizing hyperparameter values ##

import matplotlib.pyplot as plt
%matplotlib inline

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
    
plt.scatter(x=hyper_params, y=mse_values)
plt.show()

## 5. Varying features and hyperparameters ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params = list(range(1, 21))
mse_values = []
features = train_df.columns.tolist()
features.remove('price')

train_features = train_df[features]
train_target = train_df['price']

test_features = test_df[features]
test_target = test_df['price']

for i in hyper_params:
    knn = KNeighborsRegressor(algorithm='brute', n_neighbors=i)
    knn.fit(train_features, train_target)
    predictions = knn.predict(test_features)
    
    mse = mean_squared_error(test_target, predictions)
    mse_values.append(mse)

plt.scatter(x=hyper_params, y=mse_values)
plt.show()

## 6. Practice the workflow ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error



def find_lowest_hp_mse(train_data, test_data, features, target, hyper_params):
    mse_values = []
    
    train_features = train_data[features]
    train_target = train_data[target]

    test_features = test_df[features]
    test_target = test_df[target]
    
    for i in hyper_params:
        knn = KNeighborsRegressor(algorithm='brute', n_neighbors=i)
        knn.fit(train_features, train_target)
        predictions = knn.predict(test_features)

        mse = mean_squared_error(test_target, predictions)
        mse_values.append(mse)
    
    mse_min = min(mse_values)
    hyp_min = mse_values.index(mse_min) + 1
    hyp_mse = {hyp_min:mse_min}
    
    return hyp_mse
    
hyper_params = list(range(1, 21))

features = ['accommodates', 'bathrooms']
two_hyp_mse = find_lowest_hp_mse(train_df, test_df, features, 'price', hyper_params)

features = ['accommodates', 'bathrooms', 'bedrooms']
three_hyp_mse = find_lowest_hp_mse(train_df, test_df, features, 'price', hyper_params)

print(two_hyp_mse)
print(three_hyp_mse)