## 1. Recap ##

import pandas as pd
import numpy as np
np.random.seed(1)

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings.info()

## 2. Removing features ##

drop_columns = ['room_type', 'city', 'state', 'latitude', 'longitude', 
                'zipcode', 'host_response_rate', 'host_acceptance_rate', 
                'host_listings_count']

dc_listings = dc_listings.drop(drop_columns, axis=1)
print(dc_listings.isnull().sum())

## 3. Handling missing values ##

print(dc_listings.shape)

drop_columns = ['security_deposit', 'cleaning_fee']
dc_listings.drop(drop_columns, axis=1, inplace=True)
dc_listings.dropna(inplace=True)
print(dc_listings.shape)
print(dc_listings.isnull().sum())
dc_listings.head()


## 4. Normalize columns ##

normalized_listings = (dc_listings - dc_listings.mean()) / dc_listings.std()
normalized_listings['price'] = dc_listings['price']
normalized_listings.head(3)

## 5. Euclidean distance for multivariate case ##

from scipy.spatial import distance

distance_1 = normalized_listings.iloc[0][['accommodates', 'bathrooms']]
distance_2 = normalized_listings.iloc[4][['accommodates', 'bathrooms']]

first_fifth_distance = distance.euclidean(distance_1, distance_2)
first_fifth_distance

## 7. Fitting a model and making predictions ##

from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(algorithm='brute')

train_df = normalized_listings.iloc[:2792]
test_df = normalized_listings.iloc[2792:]

train_feature = train_df[['accommodates', 'bathrooms']]
test_feature = test_df[['accommodates', 'bathrooms']]
train_target = train_df['price']

knn.fit(train_feature, train_target)
predictions = knn.predict(test_feature)

predictions[:5]

## 8. Calculating MSE using Scikit-Learn ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor(algorithm='brute')

train_df = normalized_listings.iloc[:2792]
test_df = normalized_listings.iloc[2792:]

train_features = train_df[['accommodates', 'bathrooms']]
train_target = train_df['price']

test_features = test_df[['accommodates', 'bathrooms']]
test_target = test_df['price']

knn.fit(train_features, train_target)
predictions = knn.predict(test_features)

two_features_mse = mean_squared_error(test_target, predictions)
two_features_rmse  = two_features_mse**0.5

print(two_features_mse)
print(two_features_rmse)

## 9. Using more features ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor(algorithm='brute')

train_df = normalized_listings.iloc[:2792]
test_df = normalized_listings.iloc[2792:]

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']

train_features = train_df[features]
train_target = train_df['price']

test_features = test_df[features]
test_target = test_df['price']

knn.fit(train_features, train_target)
four_predictions = knn.predict(test_features)

four_mse = mean_squared_error(test_target, four_predictions)
four_rmse  = four_mse**0.5

print(four_mse)
print(four_rmse)

## 10. Using all features ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor(algorithm='brute')

train_df = normalized_listings.iloc[:2792]
test_df = normalized_listings.iloc[2792:]

columns = train_df.columns.tolist()
columns.remove('price')

train_features = train_df[columns]
train_target = train_df['price']

test_features = test_df[columns]
test_target = test_df['price']

knn.fit(train_features, train_target)
all_features_predictions = knn.predict(test_features)

all_features_mse = mean_squared_error(test_target, all_features_predictions)
all_features_rmse  = all_features_mse**0.5

print(all_features_mse)
print(all_features_rmse)