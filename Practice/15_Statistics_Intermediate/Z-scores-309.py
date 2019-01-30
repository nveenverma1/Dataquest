## 1. Individual Values ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

import numpy as np

std = np.std(houses['SalePrice'], ddof=0)
mean = houses['SalePrice'].mean()

# Plotting KDE for SalePrice Column
limits = (houses['SalePrice'].min(), houses['SalePrice'].max())

houses['SalePrice'].plot.kde(xlim=limits)
plt.axvline(mean, color='black', label='Mean')
plt.axvline(std+mean, color='red', label='Standard deviation')
plt.axvline(220000, color= 'orange', label='220000')
plt.legend()
plt.show()

very_expensive = False

## 2. Number of Standard Deviations ##

distance = 220000 - houses['SalePrice'].mean()
print(distance)

from numpy import std
std_Saleprice = std(houses['SalePrice'], ddof=0)
print(std_Saleprice)

st_devs_away = distance/std_Saleprice
print(st_devs_away)

## 3. Z-scores ##

def calc_zscore (x, arr, smpl_bool=False):
    mean = sum(arr)/len(arr)
    
    from numpy import std
    if smpl_bool:
        std_arr = std(arr, ddof=1)
    else:
        std_arr = std(arr, ddof=0)
    
    zscore = (x-mean)/std_arr
    
    return zscore

min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

min_z = calc_zscore(min_val, houses['SalePrice'])
mean_z = calc_zscore(mean_val, houses['SalePrice'])
max_z = calc_zscore(max_val, houses['SalePrice'])

print(min_z)
print(mean_z)
print(max_z)

## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z

na_zsocre = z_score(200000, houses[houses['Neighborhood'] == 'NAmes']['SalePrice'], 0)
print(na_zsocre)

cc_zscore = z_score(200000, houses[houses['Neighborhood'] == 'CollgCr']['SalePrice'], 0)
print(cc_zscore)

ot_zscore = z_score(200000, houses[houses['Neighborhood'] == 'OldTown']['SalePrice'], 0)
print(ot_zscore)

ed_zscore = z_score(200000, houses[houses['Neighborhood'] == 'Edwards']['SalePrice'], 0)
print(ed_zscore)

st_zscore = z_score(200000, houses[houses['Neighborhood'] == 'Somerst']['SalePrice'], 0)
print(st_zscore)

best_investment = 'College Creek'

## 5. Transforming Distributions ##

mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
houses['z_prices'] = houses['SalePrice'].apply(
    lambda x: ((x - mean) / st_dev)
    )

z_mean_price = houses['z_prices'].mean()
print(z_mean_price)

z_stdev_price = houses['z_prices'].std(ddof=0)
print(z_stdev_price)

lot_area_mean = houses['Lot Area'].mean()
lot_area_st_dev = houses['Lot Area'].std(ddof = 0)
houses['z_lot_area'] = houses['Lot Area'].apply(
    lambda x: ((x - lot_area_mean) / lot_area_st_dev)
    )

z_mean_area = houses['z_lot_area'].mean()
print(z_mean_area)

z_stdev_area = houses['z_lot_area'].std(ddof=0)
print(z_stdev_area)

## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]

pop_mean = mean(population)
pop_std = std(population)

pop_z = [(x-pop_mean)/pop_std for x in population]
print(pop_z)

mean_z = mean(pop_z)
stdev_z = std(pop_z)

print(mean_z)
print(stdev_z)



## 7. Standardizing Samples ##

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
    
stdev_sample = std(standardized_sample, ddof=1)
print(stdev_sample)

## 8. Using Standardization for Comparisons ##

from numpy import std, mean

def standardize(arr):
    mean_arr = mean(arr)
    std_arr = std(arr)
    
    standard_arr = [(x-mean_arr)/std_arr for x in arr]
    return standard_arr

index_1_z = standardize(houses['index_1'])
index_2_z = standardize(houses['index_2'])

print(index_1_z[:2])
print(index_2_z[:2])

better = 'first'

## 9. Converting Back from Z-scores ##

z_transformed = [(z*10 + 50) for z in houses['z_merged']]

from numpy import mean, std
mean_transformed = mean(z_transformed)
stdev_transformed = std(z_transformed)

print(mean_transformed)
print(stdev_transformed)