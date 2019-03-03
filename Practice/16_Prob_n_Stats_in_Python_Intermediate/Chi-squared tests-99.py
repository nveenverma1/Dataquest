## 2. Calculating differences ##

female_diff = (10771-16280.5)/16280.5

male_diff = (21790-16280.5)/16280.5

## 3. Updating the formula ##

female_diff = (10771-16280.5)**2/16280.5
print(female_diff)

male_diff = (21790-16280.5)**2/16280.5
print(male_diff)

gender_chisq = male_diff + female_diff
print(gender_chisq)

## 4. Generating a distribution ##

chi_squared_values = []
import numpy as np

for i in range(1000):
    random_numbers = np.random.random(32561, )
    for j in range(len(random_numbers)):
        if random_numbers[j] < 0.5:
            random_numbers[j] = 0
        else:
            random_numbers[j] = 1
            
    unique, counts = np.unique(random_numbers, return_counts=True)
    
    male_count = counts[0]
    female_count = counts[1]
    
    male_diff = (male_count-16280.5)**2/16280.5
    female_diff = (female_count-16280.5)**2/16280.5
    
    chi_squared = male_diff + female_diff
    chi_squared_values.append(chi_squared)
    
plt.hist(chi_squared_values)
plt.show()

## 6. Smaller samples ##

female_diff = (107.71-162.805)**2/162.805
print(female_diff)

male_diff = (217.90-162.805)**2/162.805
print(male_diff)

gender_chisq = male_diff + female_diff
print(gender_chisq)

## 7. Sampling distribution equality ##

import numpy as np 
chi_squared_values = []

for i in range(1000):
    vector = np.random.random(300, )
    vector[vector<0.5] = 0
    vector[vector>0.5] = 1
    
    unique, counts = np.unique(vector, return_counts=True)
    
    male_count = counts[0]
    female_count = counts[1]
    
    male_diff = (male_count-150)**2/150
    female_diff = (female_count-150)**2/150
    
    chi_squared = male_diff + female_diff
    chi_squared_values.append(chi_squared)
    
plt.hist(chi_squared_values)
plt.show()

## 9. Increasing degrees of freedom ##

race_chisq = 0
races_chi_squared = []

observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

for i in range(5):
    chi_sqaured = (observed[i] - expected[i])**2/expected[i]
    races_chi_squared.append(chi_sqaured)
    
race_chisq = sum(races_chi_squared)

print(races_chi_squared)
print(race_chisq)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

chisquare_value, race_pvalue = chisquare(observed, expected)
print(chisquare_value, race_pvalue)