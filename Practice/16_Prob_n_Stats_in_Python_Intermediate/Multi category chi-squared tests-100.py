## 2. Calculating expected values ##

males_over50k = (0.67*0.241)*32561
males_under50k = (0.67*0.759)*32561
females_over50k = (0.33*0.241)*32561
females_under50k = (0.33*0.759)*32561

print(males_over50k)
print(males_under50k)
print(females_over50k)
print(females_under50k)

## 3. Calculating chi-squared ##

chisq_gender_income = (6662-5249.8)**2/5249.8 + (1179-2597.4)**2/2597.4 + (15128-16533.5)**2/16533.5 + (9592-8180.3)**2/8180.3

print(chisq_gender_income)

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare

observed = np.array([6662, 1179, 15128, 9592])
expected = np.array([5249.8, 2597.4, 16533.5, 8180.3])
chisq_value, pvalue_gender_income = chisquare(observed, expected)

print(chisq_value)
print(pvalue_gender_income)

## 5. Cross tables ##

import pandas

table = pandas.crosstab(income['sex'], [income['race']])
print(table)

## 6. Finding expected values ##

import pandas

table = pandas.crosstab(income['sex'], [income['race']])

from scipy.stats import chi2_contingency
chisq_value, pvalue_gender_race, df, expected = chi2_contingency(table)

print(chisq_value, pvalue_gender_race, df)
print(expected)