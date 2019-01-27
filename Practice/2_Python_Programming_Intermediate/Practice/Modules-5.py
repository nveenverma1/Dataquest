## 1. Introduction to Modules ##

import math
root = math.sqrt(99)
flr = math.floor(89.9)
print(root)
print(flr)

## 2. Importing Using An Alias ##

import math as m
root = m.sqrt(33)
print(root)

## 3. Importing A Specific Object ##

from math import *
root = sqrt(1001)
print(root)

## 4. Variables Within Modules ##

import math

print(math.pi)
a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)

print(a)
print(b)
print(c)

## 5. The CSV Module ##

import csv
f = open("nfl.csv")
csvreader = csv.reader(f)
nfl = list(csvreader)
nfl

## 6. Counting How Many Times a Team Won ##

import csv
f = open("nfl.csv", "r")
nfl = list(csv.reader(f))

patriots_wins = 0
for i in nfl:
    if i[2] == "New England Patriots":
        patriots_wins += 1
print(patriots_wins)
    
    

## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(team_str):
    no_of_wins = 0
    for i in nfl:
        if i[2] == team_str:
            no_of_wins += 1
    return no_of_wins

cowboys_wins = nfl_wins("Dallas Cowboys")
print(cowboys_wins)

falcons_wins = nfl_wins("Atlanta Falcons")
print(falcons_wins)