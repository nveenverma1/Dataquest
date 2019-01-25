## 1. Creating a Dictionary ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

over_4 = content_ratings['4+']
over_9 = content_ratings['9+']
over_12 = content_ratings['12+']
over_17 = content_ratings['17+']

                    
top_genres = {'Games' : 3862,
             'Entertainment' : 535,
             'Education' : 453,
             'Photo & Video' : 349,
              'Utilities' : 248}

number_of_gaming_apps = top_genres['Games']

## 2. Alternative Way of Creating a Dictionary ##

content_ratings = {}
content_ratings['4+'] = 4433 
content_ratings['9+'] = 987
content_ratings['12+'] = 1155
content_ratings['17+'] = 622

over_12_n_apps = content_ratings['12+']

top_genres = {}

top_genres['Games'] = 3862 
top_genres['Entertainment'] = 535
top_genres['Education'] = 453
top_genres['Photo & Video'] = 349 
top_genres['Utilities'] = 248

n_apps_education = top_genres['Education']

## 3. Key-Value Pairs ##

practice1 = {1: 1, 
             2 : 'one', 
             3: ['3'], 
             4: True, 
             5: 5.0, 
             6:{1:'one'}}

practice2 = {1 : 1,
            'one' : 1,
            False : 1,
            5.0 : 1,
            #['one'] : 1,
            #{"one" : 1} : 'five'
            }

print(hash(0))
print(hash(1))
print(hash(2))
print(hash(3))
print(hash(100))
print(hash(1.3))
print(hash(0.222))
print(hash('a_string'))
print(hash('one + two'))
print(hash(True))
print(hash(False))
#print(hash([1, 2, 3]))
#print(hash({'ten' : 10}))

## 4. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

is_in_dictionary_1 = '4+' in content_ratings
is_in_dictionary_2 = '20+' in content_ratings
is_in_dictionary_3 = 4433 in content_ratings
is_in_dictionary_4 = 987 in content_ratings

if ('17+' in content_ratings):
    result = "'17+' exists in content_ratings"
    
print(result)


## 5. Counting with Dictionaries ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {'4+' : 0,
                   '9+' : 0,
                   '12+' : 0,
                   '17+' : 0}

for row in apps_data[1:]:
    c_rating = row[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1

print(content_ratings)


## 6. Finding the Unique Values ##

content_ratings = {}
genre_counting = {}

for row in apps_data[1:]:
    c_rating = row[10]
    p_genre = row[11]
    
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1
        
    if p_genre in genre_counting:
        genre_counting[p_genre] += 1
    else:
        genre_counting[p_genre] = 1
        
print(content_ratings)
print(genre_counting)

most_common_genre = 'a'
max_genre = 0

for k, v in genre_counting.items():
    if v > max_genre:
        max_genre = v
        most_common_genre = k
        
print(most_common_genre)



## 8. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
genre_counting = {'Social Networking': 167, 'Photo & Video': 349, 'Games': 3862, 'Music': 138, 'Reference': 64, 'Health & Fitness': 180, 'Weather': 72, 'Utilities': 248, 'Travel': 81, 'Shopping': 122, 'News': 75, 'Navigation': 46, 'Lifestyle': 144, 'Entertainment': 535, 'Food & Drink': 63, 'Sports': 114, 'Book': 112, 'Finance': 104, 'Education': 453, 'Productivity': 178, 'Business': 57, 'Catalogs': 10, 'Medical': 23}

total_number_of_apps = 7197

for k in content_ratings:
    content_ratings[k] /= total_number_of_apps
    content_ratings[k] *= 100
    
percentage_17_plus = content_ratings['17+']
percentage_15_allowed = content_ratings['4+'] + content_ratings['9+'] + content_ratings['12+']

for k in genre_counting:
    genre_counting[k] /= total_number_of_apps
    genre_counting[k] *= 100
    
percentage_games = genre_counting['Games']
percentage_non_games = 100 - percentage_games

## 9. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
genre_counting = {'Social Networking': 167, 'Photo & Video': 349, 'Games': 3862, 'Music': 138, 'Reference': 64, 'Health & Fitness': 180, 'Weather': 72, 'Utilities': 248, 'Travel': 81, 'Shopping': 122, 'News': 75, 'Navigation': 46, 'Lifestyle': 144, 'Entertainment': 535, 'Food & Drink': 63, 'Sports': 114, 'Book': 112, 'Finance': 104, 'Education': 453, 'Productivity': 178, 'Business': 57, 'Catalogs': 10, 'Medical': 23}

total_number_of_apps = 7197

c_ratings_proportions = {}
c_ratings_percentages = {}

for k in content_ratings:
    proportion = content_ratings[k]/total_number_of_apps
    percentage = proportion*100
    
    c_ratings_proportions[k] = proportion
    c_ratings_percentages[k] = percentage

genre_proportions = {}
genre_percentages = {}
    
for k in genre_counting:
    proportion = genre_counting[k]/total_number_of_apps
    percentage = proportion*100
    
    genre_proportions[k] = proportion
    genre_percentages[k] = percentage

## 10. Frequency Tables for Numerical Columns ##

data_sizes = []

for row in apps_data[1:]:
    size = float(row[2])
    data_sizes.append(size)
    
min_size = min(data_sizes)
max_size = max(data_sizes)

## 11. Filtering for the Intervals ##

ratings_list = []

for row in apps_data[1:]:
    rat = float(row[5])
    ratings_list.append(rat)
    
ratings_max = max(ratings_list)
ratings_min = min(ratings_list)

rat_sizes = {'0 - 10k' : 0,
            '10 - 100k' : 0,
            '100 - 500k' : 0,
            '500k - 1M': 0,
            '1M+' : 0}

for row in apps_data[1:]:
    rat_size = float(row[5])
    
    if rat_size <= 10000:
        rat_sizes['0 - 10k'] += 1
    elif 10000 < rat_size <= 100000:
        rat_sizes['10 - 100k'] += 1
    elif 100000 < rat_size <= 500000:
        rat_sizes['100 - 500k'] += 1
    elif 500000 < rat_size <= 1000000:
        rat_sizes['500k - 1M'] += 1
    elif rat_size > 1000000:
        rat_sizes['1M+'] += 1
        
print(rat_sizes)