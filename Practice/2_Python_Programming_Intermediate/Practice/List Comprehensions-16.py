## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for k, v in enumerate(ships):
    print(v)
    print(cars[k])
    


## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for k, v in enumerate(things):
    v.append(trees[k])
    

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [apple*2 for apple in apple_prices]
apple_prices_lowered = [apple - 100 for apple in apple_prices]

## 5. Counting Female Names ##

name_counts = {}

for i in legislators:
    if (i[3] == "F" and int(i[7]) > 1940):
        name = i[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
    
print(type(name_counts))

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

for i in values:
    a =  i is not None and i > 30
    checks.append(a)
    
checks
        

## 8. Highest Female Name Count ##

max_value = None

for i in name_counts:
    count = name_counts[i]
    if max_value is None or count > max_value:
        max_value = count

max_value

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for key, value in plant_types.items():
    print(key)
    print(value)

## 10. Finding the Most Common Female Names ##

top_female_names = []

for key, value in name_counts.items():
    if value == 2:
        top_female_names.append(key)
        
top_female_names

## 11. Finding the Most Common Male Names ##

top_male_names = []

male_name_counts = {}

for i in legislators:
    gender = "M"
    birth_year = 1940
    if i[3] == gender and i[7] > birth_year:
        name = i[1]
        if name in male_name_counts:
            male_name_counts[name] += 1
        else:
            male_name_counts[name] = 1
        
highest_male_count = None

for key, value in male_name_counts.items():
    if highest_male_count is None or highest_male_count < value:
        highest_male_count = value
        
for key, value in  male_name_counts.items():
    if value == highest_male_count:
        top_male_names.append(key)

top_male_names