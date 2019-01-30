## 1. Introduction ##

mean_new = houses_per_year['Mean Price'].mean()
mean_original = houses['SalePrice'].mean()
difference = mean_original - mean_new

print(mean_original)
print(mean_new)
print(difference)

## 2. Different Weights ##

sum_per_year = [(houses_per_year['Mean Price'][i] * houses_per_year['Houses Sold'][i]) for i in range(5)]
houses_sold = houses_per_year['Houses Sold'].sum()

weighted_mean = sum(sum_per_year)/houses_sold
mean_original = houses['SalePrice'].mean()

difference = round(weighted_mean, 10) - round(mean_original, 10)

## 3. The Weighted Mean ##

import numpy as np

def calc_weighted_mean(items, weights):
    weighted_items = [items[i]*weights[i] for i in range(len(items))]
    weighted_mean = sum(weighted_items)/sum(weights)
    return weighted_mean

weighted_mean_function = calc_weighted_mean(houses_per_year['Mean Price'], houses_per_year['Houses Sold'])
print(weighted_mean_function)

weighted_mean_numpy = np.average(houses_per_year['Mean Price'], weights=houses_per_year['Houses Sold'])
print(weighted_mean_numpy)

equal = (round(weighted_mean_function, 10) == round(weighted_mean_numpy, 10))
print(equal)

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']

median1 = 23
median2 = 55
median3 = 32

## 5. Distributions with Even Number of Values ##

rms_abv_grd = houses['TotRms AbvGrd'].copy()
rms_abv_grd.replace('10 or more', 10, inplace=True)
rms_abv_grd = rms_abv_grd.astype(int)
rms_abv_grd.sort_values(inplace=True)
print(rms_abv_grd.head())

middle_indices = [int(len(rms_abv_grd)/2), int(len(rms_abv_grd)/2 + 1)]
print(middle_indices)

middle_values = rms_abv_grd.iloc[middle_indices]
print(middle_values)

median = middle_values.mean()
print(median)

## 6. The Median as a Resistant Statistic ##

import matplotlib.pyplot as plt

houses['Lot Area'].plot.box()
plt.show()

houses['SalePrice'].plot.box()
plt.show()

lotarea_mean = houses['Lot Area'].mean()
lotarea_median = houses['Lot Area'].median()

saleprice_mean = houses['SalePrice'].mean()
saleprice_median = houses['SalePrice'].median()

lotarea_difference = lotarea_mean - lotarea_median
print(lotarea_difference)

saleprice_difference = saleprice_mean - saleprice_median
print(saleprice_difference)

## 7. The Median for Ordinal Scales ##

mean = houses['Overall Cond'].mean()
median = houses['Overall Cond'].median()

print(mean)
print(median)

houses['Overall Cond'].plot.hist()
plt.show()

more_representative = 'mean'