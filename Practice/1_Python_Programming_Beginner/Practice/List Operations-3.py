## 2. Parsing the File ##

weather_open = open("la_weather.csv", "r")
weather_read = weather_open.read()
#print(weather_read)
weather_list = weather_read.split("\n")
#print(weather_list)
weather_data = []
for item in weather_list:
    new_item = item.split(",")
    weather_data.append(new_item)
print(weather_data[0:10])

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for item in weather_data:
    weather.append(item[1])
print(weather)

## 4. Counting the Items in a List ##

count = 0
for item in weather:
    count += 1
print(count)

## 5. Removing the Header ##

new_weather = weather[1:len(weather)]
print(len(new_weather))

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for item in weather_types:
    found = item in new_weather
    weather_type_found.append(found)
print(weather_type_found)