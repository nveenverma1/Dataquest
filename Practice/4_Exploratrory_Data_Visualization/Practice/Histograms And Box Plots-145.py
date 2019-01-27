## 1. Introduction ##

import pandas as pd
import matplotlib.pyplot as plt
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm_reviews = reviews[cols]
norm_reviews[:5]

## 2. Frequency Distribution ##

fandango_distribution = norm_reviews['Fandango_Ratingvalue'].value_counts().sort_index()

imdb_distribution = norm_reviews['IMDB_norm'].value_counts().sort_index()

print(fandango_distribution)
print(imdb_distribution)

## 4. Histogram In Matplotlib ##

fig, ax = plt.subplots()

ax.hist(norm_reviews['Fandango_Ratingvalue'], range=(0,5))
plt.title("Fandango_Ratingvalue Histogram")
plt.show()

## 5. Comparing histograms ##

fig = plt.figure(figsize=(12, 14))

titles = ['Distribution of Fandango Ratings', 
          'Distribution of Rotten Tomatoes Ratings',
          'Distribution of Metacritic Ratings',
         'Distribution of IMDB Ratings']
num_cols1 = ['RT_user_norm',
            'Metacritic_user_nom',
             'Metacritic_user_nom',
            'IMDB_norm']

for i in range(4):
    ax = fig.add_subplot(4, 1, i+1)
    ax.hist(norm_reviews[num_cols1[i]], bins=20, range=(0,5))
    ax.set_ylim(0,50)
    ax.set_title(titles[i])
    
plt.show()

## 7. Box Plot ##

fig, ax = plt.subplots()

ax.boxplot(norm_reviews['RT_user_norm'])
ax.set_ylim(0, 5)
ax.set_xticklabels("Rotten Tomatoes")
plt.show()

## 8. Multiple Box Plots ##

fig, ax = plt.subplots()

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
ax.boxplot(norm_reviews[num_cols].values)
ax.set_ylim(0, 5)
ax.set_xticklabels(num_cols, rotation=90)
plt.show()