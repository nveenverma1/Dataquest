## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

total_days = bikes.shape[0]
days_over_threshold = bikes[bikes['cnt'] > 5000].shape[0]

prob_over_5000 = days_over_threshold/total_days
print(prob_over_5000)

## 4. Computing the distribution ##

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))

def calc_prob(p, q, N, k):
    import math
    
    # Calculating number of combinations
    numerator = math.factorial(N)
    denominator = math.factorial(k) * math.factorial(N-k)
    total_comb = numerator/denominator
    
    # Calculating total probability
    term_1 = p**k
    term_2 = q**(N-k)
    
    return term_1 * term_2 * total_comb

outcome_probs = []

for i in outcome_counts:
    outcome_i = calc_prob(0.39, 0.61, 30, i)
    outcome_probs.append(outcome_i)
    
print(outcome_probs)

## 5. Plotting the distribution ##

import matplotlib.pyplot as plt

# The most likely number of days is between 10 and 15.
plt.bar(outcome_counts, outcome_probs)
plt.show()

## 6. Simplifying the computation ##

import scipy
from scipy import linspace
from scipy.stats import binom
import matplotlib.pyplot as plt

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)
dist = binom.pmf(outcome_counts, 30, 0.39)

# Plotting binomial distribution
plt.bar(outcome_counts, dist)
plt.show()


## 8. Computing the mean of a probability distribution ##

dist_mean = 30*0.39

## 9. Computing the standard deviation ##

import math
dist_stdev = math.sqrt(30*0.39*0.61) 

## 10. A different plot ##

# Enter your answer here.
from scipy import linspace
from scipy.stats import binom

outcome_counts = linspace(0, 10, 11)
dist = binom.pmf(outcome_counts, 10, 0.39)
plt.bar(outcome_counts, dist)
plt.show()

outcome_counts = linspace(0, 100, 101)
dist = binom.pmf(outcome_counts, 100, 0.39)
plt.bar(outcome_counts, dist)
plt.show()


## 11. The normal distribution ##

# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
outcome_counts = scipy.linspace(0,100,101)

# Create a probability mass function along the outcome_counts.
outcome_probs = binom.pmf(outcome_counts,100,0.39)

# Plot a line, not a bar chart.
plt.plot(outcome_counts, outcome_probs)
plt.show()

## 12. Cumulative density function ##

from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)
print(outcome_counts, '\n')

# Create the cumulative binomial probabilities, one for each entry in outcome_counts.
dist = binom.cdf(outcome_counts,30,0.39)
print(dist, '\n')

# Plotting the CDF
plt.plot(outcome_counts, dist)
plt.show()

## 14. Faster way to calculate likelihood ##

left_16 = binom.cdf(16, 30, 0.39)
right_16 = 1 - left_16

print(left_16)
print(right_16)