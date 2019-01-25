## 3. Psycopg2 ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
print(cur)
conn.close()

## 4. Creating a table ##

import psycopg2
conn = psycopg2.connect("dbname= dq user=dq")
cur = conn.cursor()
template = '''
CREATE TABLE notes (
    id integer PRIMARY KEY,
    body text,
    title text
);
'''
cur.execute(template)
conn.close()

## 5. SQL Transactions ##

conn = psycopg2.connect("dbname=dq user=dq")
template = '''
CREATE TABLE notes (
id integer PRIMARY KEY,
body text,
title text
);
'''
cur = conn.cursor()
cur.execute(template)
conn.commit()
conn.close()


## 7. Executing queries ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()

template1 = '''
INSERT INTO notes
VALUES (
    1, 'Do more missions on Dataquest', 'Dataquest reminder'
);
'''

template2 = '''
SELECT * FROM notes;
'''

#cur.execute(template1)
cur.execute(template2)
print(cur.fetchall())
conn.close()

## 8. Creating a database ##

conn = psycopg2.connect("dbname = dq user=dq")
conn.autocommit = True
cur = conn.cursor()

template = '''
CREATE DATABASE income OWNER dq;
'''

cur.execute(template)
conn.close()

## 9. Deleting a database ##

conn = psycopg2.connect('dbname = dq user = dq')
conn.autocommit = True
cur = conn.cursor()

template = '''
DROP DATABASE income;
'''

cur.execute(template)
conn.close()