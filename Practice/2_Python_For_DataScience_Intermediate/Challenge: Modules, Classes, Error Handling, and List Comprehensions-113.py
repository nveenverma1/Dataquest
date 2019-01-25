## 2. Introduction to the Data ##

import csv

nfl_suspensions1 = list(csv.reader(open("nfl_suspensions_data.csv", "r")))
nfl_suspensions = nfl_suspensions1[1:]

years = {}

for i in nfl_suspensions:
    row_year = i[5]
    if row_year in years:
        years[row_year] += 1
    else:
        years[row_year] = 1

print(years)

## 3. Unique Values ##

unique_teams = [i[1] for i in nfl_suspensions]
unique_teams = set(unique_teams)

unique_games = [i[2] for i in nfl_suspensions]
unique_games = set(unique_games)

unique_games
unique_teams


## 4. Suspension Class ##

class Suspension:
    def __init__(self, list):
        self.name = list[0]
        self.team = list[1]
        self.games = list[2]
        self.year = list[5]
        
third_suspension = Suspension(nfl_suspensions[2])
print(third_suspension.name)
        

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
            
    def get_year(self):
        return self.year
    
missing_year = Suspension(nfl_suspensions[22])

twenty_third_year = missing_year.get_year()

twenty_third_year
        