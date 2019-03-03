## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

plt.hist(weight_lost_a, label='Weights A')
plt.hist(weight_lost_b, label='Weights B')
plt.legend()
plt.show()

print(weight_lost_a)
print(weight_lost_b)

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation test ##

mean_difference = 2.52

mean_differences = []

for i in range(1000):
    group_a = []
    group_b = []
    for j in all_values:
        val = np.random.rand()
        if val >= 0.5:
            group_a.append(j)
        else:
            group_b.append(j)
    
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
    mean_differences.append(iteration_mean_difference)
    
print(mean_differences[:50])

plt.hist(mean_differences)
plt.show()
            

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}

for i in mean_differences:
    if sampling_distribution.get(i, False):
        sampling_distribution[i] += 1
    else:
        sampling_distribution[i] = 1
        
print(sampling_distribution)

## 8. P value ##

frequencies = []

for k, v in sampling_distribution.items():
    if k >= 2.52:
        frequencies.append(v)

print(frequencies)

p_value = np.sum(frequencies)/1000
print(p_value)
