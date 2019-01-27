## 3. Populations and Samples ##

question1 = ''
question2 = ''
question3 = ''
question4 = ''
question5 = ''
question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')

parameter = wnba['Games Played'].max()
sample = wnba['Games Played'].sample(30, random_state = 1)
statistic = sample.max()
sampling_error = parameter - statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')
population_mean = wnba['PTS'].mean()
sample_means = []

for i in range(100):
    sample = wnba['PTS'].sample(10, random_state = i)
    sample_means.append(sample.mean())

plt.scatter(range(1, 101), sample_means)
plt.axhline(population_mean)
plt.show()

## 7. Stratified Sampling ##

wnba['PTG'] = wnba['PTS']/wnba['Games Played']

wnba_pos = {}
points_per_pos = {}

unique_positions = [i for i in wnba['Pos'].unique()]

for i in unique_positions:
    wnba_pos[i] = wnba[wnba['Pos'] == i]

for k, v in wnba_pos.items():
    sample = v['PTG'].sample(10, random_state = 0)
    points_per_pos[k] = sample.mean()
    
position_most_points = max(points_per_pos, key = points_per_pos.get)
print(position_most_points)


## 8. Proportional Stratified Sampling ##

print(wnba['Games Played'].value_counts(bins = 3, normalize = True) * 100)
import matplotlib.pyplot as plt

games_under_12 = wnba[wnba['Games Played'] <= 12]
games_13_22 = wnba[(wnba['Games Played'] > 12) & (wnba['Games Played'] <= 22)]
games_above_22 = wnba[wnba['Games Played'] > 22]

proportional_mean = []
    
for i in range(100):
    sample_one = games_under_12.sample(1, random_state = i)
    sample_two = games_13_22.sample(2, random_state = i)
    sample_seven = games_above_22.sample(7, random_state = i)
    
    final_sample = pd.concat([sample_one,
                              sample_two,
                              sample_seven])
    proportional_mean.append(final_sample['PTS'].mean())
    
plt.scatter(range(1, 101), proportional_mean)
plt.axhline(wnba['PTS'].mean())
plt.show()

## 9. Choosing the Right Strata ##

print(wnba['MIN'].value_counts(bins = 3, normalize = True) * 100)

played_under_347 = wnba[wnba['MIN'] <= 347]
played_348_683 = wnba[(wnba['MIN'] > 347) & (wnba['MIN'] <= 683)]
played_above_683 = wnba[wnba['MIN'] > 683]

proportional_mean = []
    
for i in range(100):
    sample_one = played_under_347.sample(4, random_state = i)
    sample_two = played_348_683.sample(4, random_state = i)
    sample_seven = played_above_683.sample(4, random_state = i)
    
    final_sample = pd.concat([sample_one,
                              sample_two,
                              sample_seven])
#     print(final_sample['MIN'].head())
    proportional_mean.append(final_sample['PTS'].mean())
    
plt.scatter(range(1, 101), proportional_mean)
plt.yticks([50, 100, 150, 200, 250, 300, 350])
plt.axhline(wnba['PTS'].mean())
plt.show()

## 10. Cluster Sampling ##

unique_teams = wnba['Team'].unique()
team_clusters = {}

for i in unique_teams:
    team_clusters[i] = wnba[wnba['Team'] == i]

random_clusters = pd.Series(wnba['Team'].unique()).sample(4, random_state = 0)
random_list = []

for i in random_clusters:
    random_list.append(team_clusters[i])

final_df = pd.concat(random_list)

sampling_error_height = wnba['Height'].mean() - final_df['Height'].mean()
sampling_error_age = wnba['Age'].mean() - final_df['Age'].mean()
sampling_error_BMI = wnba['BMI'].mean() - final_df['BMI'].mean()
sampling_error_points = wnba['PTS'].mean() - final_df['PTS'].mean()