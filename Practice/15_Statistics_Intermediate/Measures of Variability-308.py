## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

def calc_range(arr):
    min_arr = min(arr)
    max_arr = max(arr)
    return max_arr - min_arr

range_by_year = {}

years = houses['Yr Sold']

for year in years:
    if year not in range_by_year:
        range_by_year[year] = calc_range(houses[houses['Yr Sold'] == year]['SalePrice'])
    else:
        pass
    
print(range_by_year)

one = False
two = True

## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]

def calc_avg_distance(arr):
    arr_mean = np.array(C).mean()
    distances = []
    
    for i in arr:
        distances.append(arr_mean - i)
        
    dist_mean = np.array(distances).mean()
    return dist_mean

avg_distance = calc_avg_distance(C)
print(avg_distance)

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]

def calc_mad(arr):
    arr_mean = np.array(C).mean()
    distances = []
    
    for i in arr:
        distances.append(abs(arr_mean - i))
        
    dist_mean = np.array(distances).mean()
    return dist_mean

mad = calc_mad(C)
print(mad)

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]

def calc_variance(arr):
    arr_mean = np.array(C).mean()
    distances = []
    
    for i in arr:
        distances.append((arr_mean - i)**2)
        
    dist_mean = np.array(distances).mean()
    return dist_mean

variance_C = calc_variance(C)
print(variance_C)

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

C = [1,1,1,1,1,1,1,1,1,21]

def calc_sd(arr):
    arr_mean = np.array(C).mean()
    distances = []
    
    for i in arr:
        distances.append((arr_mean - i)**2)
        
    dist_mean = np.array(distances).mean()
    return sqrt(dist_mean)

standard_deviation_C = calc_sd(C)
print(standard_deviation_C)

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

std_dev = standard_deviation(houses['SalePrice'])

std_dev_by_year = {}

years = houses['Yr Sold']

for year in years:
    if year not in std_dev_by_year:
        std_dev_by_year[year] = standard_deviation(houses[houses['Yr Sold'] == year]['SalePrice'])
    else:
        pass

print(std_dev_by_year, '\n')

greatest_variability = max(std_dev_by_year, key=std_dev_by_year.get)
print(greatest_variability)

lowest_variability = min(std_dev_by_year, key=std_dev_by_year.get)
print(lowest_variability)

## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

bigger_spread = 'sample 2'

st_dev1 = standard_deviation(sample1)
print('Sample 1 Std. Dev.', st_dev1)

st_dev2 = standard_deviation(sample2)
print('Sample 2 Std. Dev.', st_dev2)

## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

prices = houses['SalePrice']
st_devs = []

for i in range(5000):
    Sample = prices.sample(10, random_state = i)
    st_dev = standard_deviation(Sample)
    st_devs.append(st_dev)
    
import matplotlib.pyplot as plt

plt.hist(st_devs)
plt.axvline(standard_deviation(houses['SalePrice']))
plt.show()

## 9. Bessel's Correction ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / (len(distances)-1)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)
    
plt.hist(st_devs)
plt.axvline(standard_deviation(houses['SalePrice']))
plt.show()

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var

pandas_stdev = sample['SalePrice'].std()
numpy_stdev = std(sample['SalePrice'], ddof=1)
print(pandas_stdev)

equal_stdevs = (pandas_stdev == numpy_stdev)
print(equal_stdevs)

pandas_var = sample['SalePrice'].var()
numpy_var = var(sample['SalePrice'], ddof=1)
print(pandas_var)

equal_vars = (pandas_var == numpy_var)
print(equal_vars)

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]

# Calculating Population Std dev and Variance
from numpy import std, var

pop_var = var(population)
pop_std = std(population)

# Calculating Sample Std dev and Variance
def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / (len(distances)-1)
    
    return (variance, sqrt(variance))


variances = []
st_devs = []

for i in samples:
    st_dev_n_var = standard_deviation(i)
    
    variances.append(st_dev_n_var[0])
    st_devs.append(st_dev_n_var[1])
    

from statistics import mean

equal_var = (pop_var == mean(variances))
equal_stdev = (pop_std == mean(st_devs))

print(equal_var)
print(equal_stdev)