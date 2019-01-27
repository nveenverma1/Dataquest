## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
ft = unrate[:12]
plt.plot(ft['DATE'], ft['VALUE'])
plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Rate')
plt.show()

## 3. Matplotlib Classes ##

print(2)

## 5. Adding Data ##

import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ft = unrate[:12]
ax1.plot(ft['DATE'], ft['VALUE'])

st = unrate[12:24]
ax2.plot(ft['DATE'], ft['VALUE'])
plt.show()



## 6. Formatting And Spacing ##

import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ft = unrate[:12]
ax1.plot(ft['DATE'], ft['VALUE'])

st = unrate[12:24]
ax2.plot(ft['DATE'], ft['VALUE'])
plt.show()



## 7. Comparing Across More Years ##

fig = plt.figure(figsize=(18,18))
unrate['MONTH'] = unrate['DATE'].dt.month

for i in range(5):
    ax = fig.add_subplot(5,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset['DATE'], subset['VALUE'])
   

plt.show()

## 8. Overlaying Line Charts ##

fig = plt.figure(figsize=(6, 3))
unrate['MONTH'] = unrate['DATE'].dt.month

for i in range(2):
    #ax = fig.add_subplot(2, 1, i+1)
    if i == 0:
        plt.plot(unrate[i*12:(i+1)*12]['MONTH'], unrate[i*12:(i+1)*12]['VALUE'], c='red')
    else:
        plt.plot(unrate[i*12:(i+1)*12]['MONTH'], unrate[i*12:(i+1)*12]['VALUE'], c='blue')
        
plt.show()
    

## 9. Adding More Lines ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i])
    
plt.show()

## 10. Adding A Legend ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
labels = [1948, 1949, 1950, 1951, 1952]
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=labels[i])

plt.legend(loc="upper left")
plt.show()

## 11. Final Tweaks ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.show()