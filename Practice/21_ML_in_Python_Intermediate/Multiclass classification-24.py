## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")
unique_regions = cars['origin'].unique()
print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)

dummy_years = pd.get_dummies(cars['year'], prefix='year')
cars = pd.concat([cars, dummy_years], axis=1)

cars.drop(['cylinders', 'year'], axis=1, inplace=True)
cars.head()

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]

seperator = int(len(shuffled_cars)*0.7)

train = shuffled_cars[:seperator]
test = shuffled_cars[seperator:]

## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}

cols = [c for c in cars.columns if c.startswith('cyl') or c.startswith('year')]


for item in unique_origins:
    model = LogisticRegression(solver='lbfgs')
    
    X_train = train[cols]
    y_train = train['origin'] == item
    
    model.fit(X_train, y_train)
    models[item] = model
    
models

## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)

for item in unique_origins:
    testing_probs[item] = models[item].predict_proba(test[cols])[:, 1]
    
testing_probs.head()

## 6. Choose the origin ##

predicted_origins = testing_probs.idxmax(axis=1)
predicted_origins.head()