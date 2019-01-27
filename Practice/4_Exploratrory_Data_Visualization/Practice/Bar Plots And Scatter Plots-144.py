## 2. Introduction to the data ##

import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv("fandango_scores.csv")
norm_reviews = reviews.loc[:,['FILM', 'RT_user_norm', 
                          'Metacritic_user_nom', 
                          'IMDB_norm', 'Fandango_Ratingvalue', 
                          'Fandango_Stars']]
norm_reviews[:1]

## 4. Creating Bars ##

fig, ax = plt.subplots()

from numpy import arange
bar_positions = arange(5) + 0.75
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews[num_cols].iloc[0].values

ax.bar(bar_positions, bar_heights)
plt.show()

## 5. Aligning Axis Ticks And Labels ##

fig, ax = plt.subplots()

bar_position = arange(5) + 0.75
bar_height = norm_reviews[num_cols].iloc[0].values

ax.bar(bar_position, bar_height, 0.5)

tick_positions = range(1, 6)
ax.set_xticks(tick_positions)

ax.set_xticklabels(num_cols)

plt.xlabel("Rating Source")
plt.ylabel("Average Rating")
plt.title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.show()

## 6. Horizontal Bar Plot ##

fig, ax = plt.subplots()

bar_position = arange(5) + 0.75
bar_height = norm_reviews[num_cols].iloc[0].values

ax.barh(bar_position, bar_height, 0.5, align="edge")

ax.set_yticklabels(num_cols)
ax.set_yticks(range(1, 6))

# ax.set_yticks(range(1, 6))
plt.ylabel("Rating Source")
plt.xlabel("Average Rating")


plt.title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.show()


## 7. Scatter plot ##

fig, ax = plt.subplots()

ax.scatter(norm_reviews['Fandango_Ratingvalue'], 
       norm_reviews['RT_user_norm'])

ax.set_xlabel("Fandango")
ax.set_ylabel("Rotten Tomatoes")

plt.title("Fandango VS Rotten Tomatoes")
plt.show()

## 8. Switching axes ##

fig = plt.figure(figsize=(6, 10))

ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.scatter(norm_reviews['Fandango_Ratingvalue'],
            norm_reviews['RT_user_norm'])
ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")

ax2.scatter(norm_reviews['RT_user_norm'],
            norm_reviews['Fandango_Ratingvalue'])
ax2.set_xlabel("Rotten Tomatoes")
ax2.set_ylabel("Fandango")

plt.show()

## 9. Benchmarking correlation ##

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.scatter(norm_reviews["Fandango_Ratingvalue"], norm_reviews["RT_user_norm"])
ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)
ax1.set_title('f vs. r')

ax2.scatter(norm_reviews["Fandango_Ratingvalue"], norm_reviews["Metacritic_user_nom"])
ax2.set_xlabel("Fandango")
ax2.set_ylabel("Metacritic")
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)
ax2.set_title('f vs. m')

ax3.scatter(norm_reviews["Fandango_Ratingvalue"], norm_reviews["IMDB_norm"])
ax3.set_xlabel("Fandango")
ax3.set_ylabel("IMDB")
ax3.set_xlim(0, 5)
ax3.set_ylim(0, 5)

plt.show()