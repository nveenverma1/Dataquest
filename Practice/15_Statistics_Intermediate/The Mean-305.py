## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]

import numpy as np

distribution_np = np.array(distribution)
mean = distribution_np.mean()

center = ((distribution[0] + distribution[6])/2 == mean)
print(center)

less = [abs(i-mean) for i in distribution if (i < mean)]
print(np.sum(less))

more = [abs(i-mean) for i in distribution if (i > mean)]
print(np.sum(more))

equal_distances = (np.sum(less) == np.sum(more))

## 3. The Mean as a Balance Point ##

import numpy as np
from numpy.random import randint, seed
equal_distances = 0

for i in range(5000):
    np.random.seed(i)
    distribution = randint(1000, size=10)
    mean = distribution.mean()
    sum_below = round(np.array([abs(i-mean) for i in distribution if (i < mean)]).sum(), 1)
    sum_above = round(np.array([abs(i-mean) for i in distribution if (i > mean)]).sum(), 1)
    equal_distances += 1
    
        
print(equal_distances)

## 4. Defining the Mean Algebraically ##

one = False
two = False
three = False

## 5. An Alternative Definition ##

def calc_mean(arr):
    mean = 0
    i = 1
    for _ in range(len(arr)):
        mean += arr[i-1]
        i += 1
    return mean/len(arr)


distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

mean_1 = calc_mean(distribution_1)
mean_2 = calc_mean(distribution_2)
mean_3 = calc_mean(distribution_3)

## 6. Introducing the Data ##

import pandas as pd

houses = pd.read_csv('AmesHousing_1.txt', sep = '\t')

one = True
two = False
three = True

## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)

function_mean = mean(houses['SalePrice'])
pandas_mean = houses['SalePrice'].mean()

means_are_equal = (function_mean == pandas_mean)

## 8. Estimating the Population Mean ##

import matplotlib.pyplot as plt

pop_mean = houses['SalePrice'].mean()
sampling_errors = []
size = 5
sampling_sizes = [size]

for i in range(0, 101):
    counter += 1
    Sample = houses['SalePrice'].sample(n = size, random_state=i)
    size += 29
    sample_mean = Sample.mean()
    sampling_error = pop_mean - sample_mean
    sampling_errors.append(sampling_error)    
    sampling_sizes.append(size)
    
plt.scatter(sampling_sizes[:-1], sampling_errors)
plt.axhline()
plt.axvline(x=2930)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')
plt.show()

## 9. Estimates from Low-Sized Samples ##

sampling_errors = []
prices = houses['SalePrice']
pop_mean = prices.mean()

for i in range(10000):
    Sample = prices.sample(n=100, random_state=i)
    sample_mean = Sample.mean()
    sampling_errors.append(sample_mean)
    
plt.hist(sampling_errors)
plt.axvline(pop_mean)
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.xlim(0,500000)
plt.show()

## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]
pop_mean = mean(population)
print(pop_mean)

samples = [[3, 7], [3, 2], [7, 2], 
           [7, 3], [2, 3], [2, 7]]
sample_means = []

for sample in samples:
    sample_means.append(mean(sample))
    
mean_of_sample_means = mean(sample_means)
print(mean_of_sample_means)

unbiased = (pop_mean == mean_of_sample_means)
print(unbiased)