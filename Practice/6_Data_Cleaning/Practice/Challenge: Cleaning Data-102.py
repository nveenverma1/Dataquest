## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
print(avengers.head(5))

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = avengers[avengers['Year']>=1960]

avengers['Year'].hist()
true_avengers['Year'].hist()
plt.show()

## 5. Consolidating Deaths ##

cols = ['Death' + str(i) for i in range(1,6)]
true_avengers['Deaths'] = (true_avengers[cols] == 'YES').sum(axis=1)
print(true_avengers)

## 6. Verifying Years Since Joining ##

def get_accuracy(row):
    accurate_age = 2015 - row['Year']
    if (row['Years since joining'] == accurate_age):
        return 1
    else:
        return 0

true_avengers['k'] = true_avengers.apply(get_accuracy, axis=1)
joined_accuracy_count = true_avengers['k'].sum(axis=0)
print(joined_accuracy_count)
print(true_avengers.shape[0])