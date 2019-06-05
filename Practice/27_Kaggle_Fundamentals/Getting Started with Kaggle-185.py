## 1. Introduction to Kaggle ##

import pandas as pd

test = pd.read_csv("test.csv")
test_shape = test.shape
print(test_shape)

train  = pd.read_csv('train.csv')
train_shape = train.shape
print(test_shape)

## 2. Exploring the Data ##

import matplotlib.pyplot as plt

sex_pivot = train.pivot_table(index="Sex",values="Survived")
sex_pivot.plot.bar()
plt.show()

## Pclass
pclass_pivot = train.pivot_table(index='Pclass', values='Survived')
pclass_pivot.plot.bar()
plt.show()

## 3. Exploring and Converting the Age Column ##

def process_age(df,cut_points,label_names):
    df["Age"] = df["Age"].fillna(-0.5)
    df["Age_categories"] = pd.cut(df["Age"],cut_points,labels=label_names)
    return df

cut_points = [-1, 0, 5, 12, 18, 35, 60, 100]
label_names = ['Missing', 'Infant', 'Child', 'Teenager', 
               'Young Adult', 'Adult', 'Senior']

train = process_age(train, cut_points, label_names)
test = process_age(test, cut_points, label_names)

age_pivot = train.pivot_table(index='Age_categories', values='Survived')
age_pivot.plot.bar()
plt.show()

## 4. Preparing our Data for Machine Learning ##

# def create_dummies(df,column_name):
#     dummies = pd.get_dummies(df[column_name],prefix=column_name)
#     df = pd.concat([df,dummies],axis=1)
#     return df

# train = create_dummies(train,"Pclass")
# test = create_dummies(test,"Pclass")

def create_dummies(df, column_name):
    dummies = pd.get_dummies(df[column_name], prefix=column_name)
    df = pd.concat([df, dummies], axis=1)
    return df

cols_to_dummy = ['Pclass', 'Sex', 'Age_categories']

for item in cols_to_dummy:
    train = create_dummies(train, item)
    test = create_dummies(test, item)
    
train.head()

## 5. Creating Our First Machine Learning Model ##

columns = ['Pclass_1', 'Pclass_2', 'Pclass_3', 'Sex_female', 'Sex_male',
       'Age_categories_Missing','Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior']

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

lr.fit(train[columns], train['Survived'])


## 6. Splitting Our Training Data ##

holdout = test # from now on we will refer to this
               # dataframe as the holdout data

from sklearn.model_selection import train_test_split

columns = ['Pclass_1', 'Pclass_2', 'Pclass_3', 'Sex_female', 'Sex_male',
       'Age_categories_Missing','Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior']

all_X = train[columns]
all_y = train['Survived']

train_X, test_X, train_y, test_y = train_test_split(all_X, all_y, test_size=0.2, random_state=0)



## 7. Making Predictions and Measuring their Accuracy ##

from sklearn.metrics import accuracy_score

lr = LogisticRegression(solver='lbfgs')
lr.fit(train_X, train_y)

predictions = lr.predict(test_X)
accuracy = accuracy_score(test_y, predictions)
print(accuracy)

## 8. Using Cross Validation for More Accurate Error Measurement ##

from sklearn.model_selection import cross_val_score
import numpy as np

lr = LogisticRegression(solver='lbfgs')
scores = cross_val_score(lr, all_X, all_y, cv=10)
accuracy = np.mean(scores)

print(scores)
print(accuracy)

## 9. Making Predictions on Unseen Data ##

columns = ['Pclass_1', 'Pclass_2', 'Pclass_3', 'Sex_female', 'Sex_male',
       'Age_categories_Missing','Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior']

lr = LogisticRegression(solver='lbfgs')
lr.fit(all_X, all_y)
holdout_predictions = lr.predict(test[columns])

## 10. Creating a Submission File ##

test_ids = test['PassengerId']
submission = pd.DataFrame({"PassengerId": test_ids, "Survived": holdout_predictions})
submission.to_csv('submission.csv', index=False)
pd.read_csv('submission.csv').head()