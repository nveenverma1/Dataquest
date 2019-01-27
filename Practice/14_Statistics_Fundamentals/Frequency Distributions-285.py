## 1. Simplifying Data ##

import pandas as pd

pd.options.display.max_rows = 200
pd.options.display.max_columns = 50

wnba = pd.read_csv("wnba.csv")
print(wnba.shape)
print(wnba.head())

## 2. Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
freq_distro_pos = wnba['Pos'].value_counts()
freq_distro_height = wnba['Height'].value_counts()
print(freq_distro_pos)
print(freq_distro_height)

## 3. Sorting Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

freq_age = wnba['Age'].value_counts()

age_ascending = freq_age.sort_index()
age_descending = freq_age.sort_index(ascending = False)

## 4. Sorting Tables for Ordinal Variables ##

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

# Type your answer below
pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts().iloc[[4, 3, 0, 2, 1, 5]]

## 5. Proportions and Percentages ##

wnba = pd.read_csv('wnba.csv')
Age_proportion = wnba['Age'].value_counts(normalize=True)
Age_percetage = wnba['Age'].value_counts(normalize=True)*100
proportion_25 = Age_proportion[25]
percentage_30 = Age_percetage[30]
percentage_over_30 = Age_percetage[Age_percetage.index >= 30].sum()
percentage_below_23 = Age_percetage[Age_percetage.index <= 23].sum()

## 6. Percentiles and Percentile Ranks ##

wnba = pd.read_csv('wnba.csv')

from scipy.stats import percentileofscore
percentile_rank_half_less = percentileofscore(wnba['Games Played'], 
                                              17, 
                                              kind = 'weak')

percentage_half_more = (100 - percentile_rank_half_less)

## 7. Finding Percentiles with pandas ##

wnba = pd.read_csv('wnba.csv')

age_describe = wnba['Age'].describe(percentiles=
                                          [0.5, 0.75, 0.95]).iloc[3:]

age_upper_quartile = age_describe['75%']
age_middle_quartile = age_describe['50%']
age_95th_percentile = age_describe['95%']
question1 = True
question2 = False
question3 = True

## 8. Grouped Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
grouped_freq_table = wnba['PTS'].value_counts(bins=10, normalize=True).sort_index(ascending=False)*100
print(grouped_freq_table)

## 9. Information Loss ##

import pandas as pd

print(wnba['MIN'].value_counts(bins=10))

## 10. Readability for Grouped Frequency Tables ##

wnba = pd.read_csv('wnba.csv')
intervals = pd.interval_range(start=0, end=600, freq=60)
#print(len(intervals))

gr_freq_table_10 = pd.Series([0 for i in range(len(intervals))], index=intervals)

for value in wnba['PTS']:
    for i in intervals:
        if value in i:
            gr_freq_table_10.loc[i] += 1
            break
            
gr_freq_table_10
print(intervals)