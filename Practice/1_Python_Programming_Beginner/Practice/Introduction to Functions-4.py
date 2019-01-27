## 1. Overview ##

f = open("movie_metadata.csv", "r")
data = f.read()

movies = data.split("\n")
movie_data = []

for item in movies:
    new_item = item.split(",")
    movie_data.append(new_item)
    
print(movie_data[0:5])
    


## 3. Writing Our Own Functions ##

#print(movie_data)
def getting_movie_names(input_lst):
    movie_list = []
    for item in input_lst:
        new_item = item[0]
        movie_list.append(new_item)
    return movie_list

movie_names = getting_movie_names(movie_data)
print(movie_names[0:5])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False

first_movie_usa = is_usa(movie_data[1])
print(first_movie_usa)

wonder_woman_usa = is_usa(wonder_woman)
print(wonder_woman_usa)

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False

def index_equals_str(input_lst, index, input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
    
wonder_woman_in_color = index_equals_str(wonder_woman, 2, "Color")
print(wonder_woman_in_color)

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_counter(input_lst, index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
        for each in input_lst:
            if each[index] == input_str:
                num_elt = num_elt + 1
        return num_elt
    
num_of_us_movies = feature_counter(movie_data, 6, "USA", header_row = True)
print(num_of_us_movies)
        
    

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(lst):
    num_japan_films = feature_counter(lst, 6, "Japan", header_row = True)
    num_color_films = feature_counter(lst, 2, "Color", header_row = True)
    num_films_in_english = feature_counter(lst, 5, "English", header_row = True)
    summary_dict = {
        "japan_films" : num_japan_films,
        "color_films" : num_color_films,
        "films_in_english" : num_films_in_english
    }
    return summary_dict

summary = summary_statistics(movie_data)
print(summary)    