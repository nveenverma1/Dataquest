## 1. Comparing Frequency Distributions ##

rookies = wnba[wnba['Exp_ordinal'] == 'Rookie']
little_xp = wnba[wnba['Exp_ordinal'] == 'Little experience']
experienced = wnba[wnba['Exp_ordinal'] == 'Experienced']
very_xp = wnba[wnba['Exp_ordinal'] == 'Very experienced']
veterans =  wnba[wnba['Exp_ordinal'] == 'Veteran']

rookie_distro = rookies['Pos'].value_counts()
little_xp_distro = little_xp['Pos'].value_counts()
experienced_distro = experienced['Pos'].value_counts()
very_xp_distro = very_xp['Pos'].value_counts()
veteran_distro = veterans['Pos'].value_counts()

print(rookie_distro)
print(little_xp_distro)
print(experienced_distro)
print(very_xp_distro)
print(veteran_distro)


## 2. Grouped Bar Plots ##

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='Exp_ordinal', 
              order = ['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'], 
              hue='Pos', hue_order = ['C', 'F', 'F/C', 'G', 'G/F'], data=wnba)
plt.show()


## 3. Challenge: Do Older Players Play Less? ##

sns.countplot(x='age_mean_relative', hue='min_mean_relative', 
              data=wnba)
plt.show()
result='rejection'

## 4. Comparing Histograms ##

import matplotlib.pyplot as plt
wnba[wnba['Age'] < 27]['MIN'].plot.hist(histtype='step', label='Young')
wnba[wnba['Age'] >= 27]['MIN'].plot.hist(histtype='step', label='Old')
plt.axvline(x = 497, label='Average')
plt.legend()
plt.show()

## 5. Kernel Density Estimate Plots ##

wnba[wnba['Age'] < 27]['MIN'].plot.kde(label='Young')
wnba[wnba['Age'] >= 27]['MIN'].plot.kde(label='Old')
plt.axvline(x=497, label='Average')
plt.legend()
plt.show()

## 7. Strip Plots ##

import seaborn as sns
import matplotlib.pyplot as plt

sns.stripplot(x='Pos', y='Weight', data=wnba, jitter=True)
plt.show()

## 8. Box plots ##

sns.boxplot(x='Pos', y='Weight', data=wnba)
plt.show()

## 9. Outliers ##

gamesp_info = wnba['Games Played'].describe()
iqr = gamesp_info['75%'] - gamesp_info['25%']
lower_bound = gamesp_info['25%'] - (1.5*iqr)
upper_bound = gamesp_info['75%'] + (1.5*iqr)

outliers_low = len(wnba[wnba['Games Played'] < 
                         lower_bound]['Games Played'])

outliers_high = len(wnba[wnba['Games Played'] > 
                         upper_bound]['Games Played']) 

print(outliers_low)
print(outliers_high)

sns.boxplot(wnba['Games Played'])
plt.show()