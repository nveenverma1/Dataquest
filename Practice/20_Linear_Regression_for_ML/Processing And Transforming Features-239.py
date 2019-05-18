## 1. Introduction ##

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

train_null_counts = train.isnull().sum()
print(train_null_counts)

train_null_counts = train_null_counts[train_null_counts == 0]
df_no_mv = train[train_null_counts.index]

df_no_mv.head()

## 2. Categorical Features ##

text_cols = df_no_mv.select_dtypes(include=['object']).columns

for col in text_cols:
    print(col+":", len(train[col].unique()))
    train[col] = train[col].astype('category')
    
train['Utilities'].cat.codes.value_counts()

## 3. Dummy Coding ##

df = pd.get_dummies(train[text_cols])

## concatenating dummy code with original train dataframe
for col in text_cols:
    dummy_col = pd.get_dummies(train[col])
    train = pd.concat([train, dummy_col], axis=1)
    train.drop(col, axis = 1, inplace=True)

train.head()

## 4. Transforming Improper Numerical Features ##

train['years_until_remod'] = train['Year Remod/Add'] - train['Year Built']

train.head()

## 5. Missing Values ##

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

train_null_counts = train.isnull().sum()

df_missing_values_cols = train_null_counts[(train_null_counts > 0) & (train_null_counts < 584)].index
df_missing_values = train[df_missing_values_cols]

df_missing_values.head()

## 6. Imputing Missing Values ##

float_cols = df_missing_values.select_dtypes('float')
float_cols = float_cols.fillna(float_cols.mean())

float_cols.isnull().sum()