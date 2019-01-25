## 1. If Statements ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    # Complete the code from here
    price = float(row[4])
    if (price == 0.0):
        free_apps_ratings.append(rating)
        
avg_rating_free = sum(free_apps_ratings)/len(free_apps_ratings)
n_free_apps = len(free_apps_ratings)

percentage_free_apps = (len(free_apps_ratings)/len(apps_data[1:]))*100

## 2. Booleans ##

a_price = 0
prices = [0, 2, 0, 0, 0]
app_and_price = [['Facebook', 0], ['Instagram', 0], ['Plants vs. Zombies', 0.99],
                 ['Minecraft: Pocket Edition', 6.99], ['Temple Run', 0],
                 ['Plague Inc.', 0.99]]

if (a_price == 0):
    print("This is free.")
    
if (a_price == 1):
    print("This is not free.")
    
free = []

for i in prices:
    if (i==0):
        free.append(i)
        
n_free_prices = len(free)

free_apps = []
for i in app_and_price:
    name = i[0]
    price = i[1]
    if (price == 0):
        free_apps.append(name)
        
print(free_apps)
    
    
    
    
    
    
    

## 3. The Average Rating of Non-free Apps ##

non_free_apps_ratings = []

for i in apps_data[1:]:
    rating = float(i[7])
    price = float(i[4])
    if (price != 0.0):
        non_free_apps_ratings.append(rating)
        
avg_rating_non_free = sum(non_free_apps_ratings)/len(non_free_apps_ratings)

'''Here we can observe that the non-free apps have an avg. rating of 3.72, whereas the free apps have an avg. rating of 3.37.

From this, we can observe that the non-free apps have an average 10% higher rating then the free apps.'''

## 4. The Average Rating of Gaming Apps ##

non_games_ratings = []

for i in apps_data[1:]:
    rating = float(i[7])
    genre = i[11]
    if (genre != 'Games'):
        non_games_ratings.append(rating)
        
avg_rating_non_games = sum(non_games_ratings)/len(non_games_ratings)

'''Here, we can observe that the avg. rating of non-game apps(3.34) is lower than the avg. rating of game apps(3.69).'''

## 5. Multiple Conditions ##

free_games_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    if (price == 0.0 and genre == 'Games'):
        free_games_ratings.append(rating)
        
avg_rating_free_games = sum(free_games_ratings)/len(free_games_ratings)

## 6. The or Operator ##

games_social_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    if (genre == 'Games' or genre == 'Social Networking'):
        games_social_ratings.append(rating)
        
avg_games_social = sum(games_social_ratings)/len(games_social_ratings)

## 7. Combining Logical Operators ##

free_games_social_ratings = []
nonfree_games_social_ratings = []
for row in apps_data[1:]: # apps_data is already saved from previous screens
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price == 0:
        free_games_social_ratings.append(rating)
        
    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        nonfree_games_social_ratings.append(rating)

# Write your code below
avg_free = sum(free_games_social_ratings)/len(free_games_social_ratings)

avg_non_free = sum(nonfree_games_social_ratings)/len(nonfree_games_social_ratings)

## 8. Comparison Operators ##

greater_than_9 = []
n_apps_more_9 = 0

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    
    if (price > 9.0):
        greater_than_9.append(rating)
        
avg_rating = sum(greater_than_9)/len(greater_than_9)
n_apps_more_9 = len(greater_than_9)
n_apps_less_9 = len(apps_data[1:]) - n_apps_more_9

## 9. The else Clause ##

for row in apps_data[1:]:
    price = float(row[4])
    if (price == 0.0):
        row.append('free')
    else:
        row.append('non-free')
        
apps_data[0].append('free_or_not')
print(apps_data[0])
print(apps_data[1:6])

## 10. The elif Clause ##

for row in apps_data[1:]:
    price = float(row[4])
    if (price == 0.0):
        row.append('free')
    elif (price > 0.0 and price < 20.0):
        row.append('affordable')
    elif (price >= 20.0 and price < 50.0):
        row.append('expensive')
    else:
        row.append('very expensive')
        
apps_data[0].append('price_label')
print(apps_data[0])
print(apps_data[1:6])