## 2. Sets ##

import csv 
f = open("legislators.csv", "r")
csvreader = csv.reader(f)
legislators = list(csvreader)
legislators = legislators[1:]

gender = []

for item in legislators:
    gender.append(item[3])
    
gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

import csv
f = open("legislators.csv", "r")
csvreader = list(csv.reader(f))
legislators = csvreader[1:]

party = []

for item in legislators:
    party.append(item[6])
party = set(party)
print(party)

## 4. Missing Values ##

import csv
f = open('legislators.csv', "r")
csvreader = list(csv.reader(f))
legislators = csvreader[1:]

for item in legislators:
    if item[3] == "":
        item[3] = "M"


## 5. Parsing Birth Years ##

import csv
f = open('legislators.csv', "r")
csvreader = list(csv.reader(f))
legislators = csvreader[1:]

birth_years = []
for item in legislators:
    parts = item[2].split("-")
    birth_years.append(parts[0])
    
print(birth_years)

## 6. Try/except Blocks ##

try:
    float("hello")
except ValueError:
    print("Error converting to float..")

## 7. Exception Instances ##

try:
    int("")
except Exception as exc:
    print(type(exc))
    print(str(type(exc)))

## 8. The Pass Keyword ##

converted_years = []
for year in birth_years:
    try:
        int_year = int(year)
        converted_years.append(int_year)
    except Exception:
        pass

## 9. Convert Birth Years to Integers ##

for item in legislators:
    parts = item[2].split("-")
    try:
        birth_year = int(parts[0])
    except Exception:
        birth_year = 0
    item.append(birth_year)
    

## 10. Fill in Years Without a Value ##

last_value = 1
for item in legislators:
    if item[7] == 0:
        item[7] = last_value
    last_value = item[7]