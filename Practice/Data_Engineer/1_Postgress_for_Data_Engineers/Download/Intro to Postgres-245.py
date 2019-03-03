## 2. Connecting to Postgres ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
print(conn)
conn.close()

## 3. Interacting with the Database ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")

query = "SELECT * FROM notes"
cursor = conn.cursor()
cursor.execute(query)

notes = cursor.fetchall()
print(notes)
conn.close()

## 4. Creating a Table ##

conn = psycopg2.connect("dbname=dq user=dq")

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users") # Dropping table if already exists

# Creating table users (id, email, name and address)
cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT, name TEXT, address TEXT);") 

## 5. SQL Transactions ##

conn = psycopg2.connect("dbname=dq user=dq")

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users") # Dropping table if already exists

# Creating table users (id, email, name and address)
cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT, name TEXT, address TEXT);") 

conn.commit()
conn.close()

## 6. Inserting the Data ##

import csv

import psycopg2
conn = psycopg2.connect('user=dq dbname=dq')
cur = conn.cursor()
cur.execute("DELETE FROM users;")

with open('user_accounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
   # rows = [x for x in reader]
    for row in reader:
        cur.execute("INSERT INTO users VALUES(%s, %s, %s, %s)", row)
    
conn.commit()    
cur.execute("SELECT * FROM users")
users = cur.fetchall()
conn.close()


## 7. Copying the Data ##

conn = psycopg2.connect("user=dq dbname=dq")
cur = conn.cursor()
cur.execute("DELETE FROM users;")

with open('user_accounts.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'users', sep=",")
    
conn.commit()
    
cur.execute("SELECT * FROM users")
users = cur.fetchall()
conn.close()

print(users[:5])