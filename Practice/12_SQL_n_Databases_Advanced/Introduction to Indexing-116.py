## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")

template = '''
pragma table_info('facts');
'''

schema = conn.execute(template).fetchall()

for row in schema:
    print(row)


## 3. Explain query plan ##

template1 = '''
explain query plan select * from facts where area > 40000;
'''

template2 = '''
explain query plan select area from facts where area > 40000;
'''

template3 = '''
explain query plan select * from facts where name = 'Czech Republic';
'''

import sqlite3
conn = sqlite3.connect('factbook.db')
query_plan_one = conn.execute(template1).fetchall()
query_plan_two = conn.execute(template2).fetchall()
query_plan_three = conn.execute(template3).fetchall()

print(query_plan_one)
print(query_plan_two)
print(query_plan_three)

## 5. Time complexity ##

cursor = conn.cursor()
template = '''
explain query plan select * from facts where id = 20;
'''

cursor.execute(template)
query_plan_four = cursor.fetchall()
print(query_plan_four)
conn.close()


## 9. All together now ##

cur = conn.cursor()
cur.execute('explain query plan select * from facts where population > 10000;')
query_plan_six = cur.fetchall()
print(query_plan_six)

cur.execute('create index if not exists pop_idx on facts(population);')

cur.execute('explain query plan select * from facts where population > 10000;')
query_plan_seven = cur.fetchall()
print(query_plan_seven)