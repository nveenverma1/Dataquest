## 1. Recap ##

import pandas as pd
loans = pd.read_csv('cleaned_loans_2007.csv')
loans.info()

## 3. Picking an error metric ##

import pandas as pd
tn_filter = (predictions == 0) &  (loans['loan_status'] == 0)
tn = len(predictions[tn_filter])

tp_filter = (predictions == 1) &  (loans['loan_status'] == 1)
tp = len(predictions[tp_filter])

fn_filter = (predictions == 0) &  (loans['loan_status'] == 1)
fn = len(predictions[fn_filter])

fp_filter = (predictions == 1) &  (loans['loan_status'] == 0)
fp = len(predictions[fp_filter])

## 5. Class imbalance ##

import pandas as pd
import numpy

# Predict that all loans will be paid off on time.
predictions = pd.Series(numpy.ones(loans.shape[0]))

tn_filter = (predictions == 0) &  (loans['loan_status'] == 0)
tn = len(predictions[tn_filter])

tp_filter = (predictions == 1) &  (loans['loan_status'] == 1)
tp = len(predictions[tp_filter])

fn_filter = (predictions == 0) &  (loans['loan_status'] == 1)
fn = len(predictions[fn_filter])

fp_filter = (predictions == 1) &  (loans['loan_status'] == 0)
fp = len(predictions[fp_filter])

fpr = fp / (fp + tn)
tpr = tp / (tp + fn)

print(fpr)
print(tpr)

## 6. Logistic Regression ##

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

features = loans.drop('loan_status', axis=1)
target = loans['loan_status']

lr.fit(features, target)
predictions = lr.predict(features)

## 7. Cross Validation ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
lr = LogisticRegression()

predictions = cross_val_predict(lr, features, target, cv=3)
predictions = pd.Series(predictions)

tn_filter = (predictions == 0) &  (loans['loan_status'] == 0)
tn = len(predictions[tn_filter])

tp_filter = (predictions == 1) &  (loans['loan_status'] == 1)
tp = len(predictions[tp_filter])

fn_filter = (predictions == 0) &  (loans['loan_status'] == 1)
fn = len(predictions[fn_filter])

fp_filter = (predictions == 1) &  (loans['loan_status'] == 0)
fp = len(predictions[fp_filter])

## Printing False Positive and True Positive Rate
fpr = fp / (fp + tn)
tpr = tp / (tp + fn)

print(fpr)
print(tpr)

## 9. Penalizing the classifier ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
lr = LogisticRegression(class_weight='balanced')

predictions = cross_val_predict(lr, features, target, cv=3)
predictions = pd.Series(predictions)

tn_filter = (predictions == 0) &  (loans['loan_status'] == 0)
tn = len(predictions[tn_filter])

tp_filter = (predictions == 1) &  (loans['loan_status'] == 1)
tp = len(predictions[tp_filter])

fn_filter = (predictions == 0) &  (loans['loan_status'] == 1)
fn = len(predictions[fn_filter])

fp_filter = (predictions == 1) &  (loans['loan_status'] == 0)
fp = len(predictions[fp_filter])

## Printing False Positive and True Positive Rate
fpr = fp / (fp + tn)
tpr = tp / (tp + fn)

print(fpr)
print(tpr)

## 10. Manual penalties ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
penalty = {
    0:10,
    1:1
}

lr = LogisticRegression(class_weight=penalty)

predictions = cross_val_predict(lr, features, target, cv=3)
predictions = pd.Series(predictions)

tn_filter = (predictions == 0) &  (loans['loan_status'] == 0)
tn = len(predictions[tn_filter])

tp_filter = (predictions == 1) &  (loans['loan_status'] == 1)
tp = len(predictions[tp_filter])

fn_filter = (predictions == 0) &  (loans['loan_status'] == 1)
fn = len(predictions[fn_filter])

fp_filter = (predictions == 1) &  (loans['loan_status'] == 0)
fp = len(predictions[fp_filter])

## Printing False Positive and True Positive Rate
fpr = fp / (fp + tn)
tpr = tp / (tp + fn)

print(fpr)
print(tpr)

## 11. Random forests ##

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict

rf  = RandomForestClassifier(class_weight='balanced', random_state = 1)

predictions = cross_val_predict(rf, features, target, cv=3)
predictions = pd.Series(predictions)

tn_filter = (predictions == 0) &  (loans['loan_status'] == 0)
tn = len(predictions[tn_filter])

tp_filter = (predictions == 1) &  (loans['loan_status'] == 1)
tp = len(predictions[tp_filter])

fn_filter = (predictions == 0) &  (loans['loan_status'] == 1)
fn = len(predictions[fn_filter])

fp_filter = (predictions == 1) &  (loans['loan_status'] == 0)
fp = len(predictions[fp_filter])

## Printing False Positive and True Positive Rate
fpr = fp / (fp + tn)
tpr = tp / (tp + fn)

print(fpr)
print(tpr)