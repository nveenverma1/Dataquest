## 1. Introduction ##

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

split_one = dc_listings.iloc[:1862]
split_two = dc_listings[1862:]

print(split_one.shape)
print(split_two.shape)

split_one.head()

## 2. Holdout Validation ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

knn = KNeighborsRegressor()
knn.fit(train_one[['accommodates']], train_one['price'])
predictions = knn.predict(test_one[['accommodates']])
iteration_one_rmse = mean_squared_error(test_one['price'], predictions) ** 0.5

knn.fit(train_two[['accommodates']], train_two['price'])
predictions = knn.predict(test_two[['accommodates']])
iteration_two_rmse = mean_squared_error(test_two['price'], predictions) ** 0.5

avg_rmse = np.array([iteration_one_rmse, iteration_two_rmse]).mean()
avg_rmse

## 3. K-Fold Cross Validation ##

dc_listings.loc[dc_listings.index[:745], 'fold'] = 1
dc_listings.loc[dc_listings.index[745:1490], 'fold'] = 2
dc_listings.loc[dc_listings.index[1490:2234], 'fold'] = 3
dc_listings.loc[dc_listings.index[2234:2978], 'fold'] = 4
dc_listings.loc[dc_listings.index[2978:3723], 'fold'] = 5

print(dc_listings['fold'].isnull().sum())
dc_listings['fold'].value_counts()

## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_data = dc_listings[dc_listings['fold'] > 1]
test_data = dc_listings[dc_listings['fold'] == 1]

knn = KNeighborsRegressor()
knn.fit(train_data[['accommodates']], train_data['price'])
labels = knn.predict(test_data[['accommodates']])

iteration_one_rmse = mean_squared_error(test_data['price'], labels) ** 0.5
iteration_one_rmse

## 5. Function for training models ##

def train_and_validate(df, folds):
    knn = KNeighborsRegressor()
    rmses = []
    
    for i in folds:
        train_data = dc_listings.loc[dc_listings['fold'] != i]
        test_data = dc_listings.loc[dc_listings['fold'] == i]
        
        knn.fit(train_data[['accommodates']], train_data['price'])
        labels = knn.predict(test_data[['accommodates']])
        
        rmse = mean_squared_error(test_data['price'], labels) ** 0.5
        rmses.append(rmse)
        
    return rmses

rmses = train_and_validate(dc_listings, list(range(1, 6)))
avg_rmse = np.mean(rmses)

print(rmses)
print(avg_rmse)    

## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

from sklearn.model_selection import cross_val_score, KFold
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

kf = KFold(n_splits=5, shuffle=True, random_state=1)
knn = KNeighborsRegressor()

mses = cross_val_score(knn, dc_listings[['accommodates']], dc_listings['price'], 
                       scoring="neg_mean_squared_error", cv=kf)

rmses = [np.abs(x)**0.5 for x in mses]
avg_rmse = np.mean(rmses)
avg_rmse

## 7. Exploring Different K Values ##

from sklearn.model_selection import cross_val_score, KFold

num_folds = [3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 21, 23]

for fold in num_folds:
    kf = KFold(fold, shuffle=True, random_state=1)
    model = KNeighborsRegressor()
    mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="neg_mean_squared_error", cv=kf)
    rmses = np.sqrt(np.absolute(mses))
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    print(str(fold), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))