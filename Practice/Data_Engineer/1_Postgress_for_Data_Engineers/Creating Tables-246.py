## 1. Describing a Table ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("SELECT * FROM ign_reviews LIMIT 0;")
print(cur.description)

## 2. Adding the id Field ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# We will use BIGINT data type for id since it takes appx. 63 bits/8 bytes of storage
cur.execute("DROP TABLE IF EXISTS ign_reviews")
cur.execute("CREATE TABLE ign_reviews (id BIGINT PRIMARY KEY);")
cur.execute("SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'ign_reviews';")
conn.commit()
print(cur.fetchall())
conn.close()

## 3. Finding the Max Length ##

import csv 

with open('ign.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    unique_words_in_score = set([row[1] for row in reader])
    
print(unique_words_in_score)

# Getting length of the longest word
max_score = max([len(x) for x in unique_words_in_score])
print(max_score)

## 4. Max String-like Datatypes ##

conn = psycopg2.connect("user=dq dbname=dq")
cur = conn.cursor()

# We will use varchar(n) data type for score_phrase since it takes appx. 63 bits/8 bytes of storage
cur.execute("DROP TABLE IF EXISTS ign_reviews")
cur.execute("CREATE TABLE ign_reviews (id BIGINT PRIMARY KEY, score_phrase varchar(11));")
cur.execute("SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'ign_reviews';")
conn.commit()
print(cur.fetchall())
conn.close()

## 5. Creating the Other String Fields ##

conn = psycopg2.connect("user=dq dbname=dq")
cur = conn.cursor()

# We will use varchar(n) data type for score_phrase since it takes appx. 63 bits/8 bytes of storage
cur.execute("DROP TABLE IF EXISTS ign_reviews")
cur.execute("""
CREATE TABLE ign_reviews (
id BIGINT PRIMARY KEY, 
score_phrase varchar(11),
title TEXT,
url TEXT,
platform VARCHAR(20),
genre VARCHAR(25));""")
cur.execute("SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'ign_reviews';")
conn.commit()
print(cur.fetchall())

## 6. Float-like Types ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
# Add your field and type here.
cur.execute("DROP TABLE IF EXISTS ign_reviews")
cur.execute("""
    CREATE TABLE ign_reviews (
        id BIGINT PRIMARY KEY,
        score_phrase VARCHAR(11),
        title TEXT,
        url TEXT,
        platform VARCHAR(20),
        genre TEXT,
        score DECIMAL(3, 2)        
    )
""")

conn.commit()

cur.execute("SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'ign_reviews';")
print(cur.fetchall())

## 7. Boolean Types ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
# Add your fields and types here.
cur.execute("DROP TABLE IF EXISTS ign_reviews")
cur.execute("""
    CREATE TABLE ign_reviews (
        id BIGINT PRIMARY KEY,
        score_phrase VARCHAR(11),
        title TEXT,
        url TEXT,
        platform VARCHAR(20),
        score DECIMAL(3, 1),
        genre TEXT,
        editors_choice BOOLEAN)""")

conn.commit()

cur.execute("SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'ign_reviews';")
print(cur.fetchall())

## 8. Date Type ##

conn = psycopg2.connect("user=dq dbname=dq")
cur = conn.cursor()

# We will use DATE data type for release_date. And, combine the 3 columns into one using INSERT 
# with string interpolation
cur.execute("DROP TABLE IF EXISTS ign_reviews")
cur.execute("""
CREATE TABLE ign_reviews (
id BIGINT PRIMARY KEY, 
score_phrase varchar(11),
title TEXT,
url TEXT,
platform VARCHAR(20),
score DECIMAL(3, 1),
genre VARCHAR(25),
editors_choice BOOLEAN,
release_date DATE);""")

from datetime import date
import csv

with open('ign.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    for row in reader:
        updated_row = row[:8]
        updated_row.append(date(int(row[8]), int(row[9]), int(row[10])))
        cur.execute("INSERT INTO ign_reviews VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", updated_row)

conn.commit()

cur.execute("SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'ign_reviews';")
print(cur.fetchall())

#conn.close()