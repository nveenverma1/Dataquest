## 1. Introduction ##

houses = pd.read_csv('AmesHousing_1.txt', sep='\t')

scale_land = 'ordinal'
scale_roof = 'nominal'
kitchen_variable = 'discrete'

## 2. The Mode for Ordinal Variables ##

def calc_mode(arr):
    values_dict = {}
    
    for item in arr:
        if item in values_dict:
            values_dict[item] += 1
        else:
            values_dict[item] = 1
            
    return max(values_dict, key = values_dict.get)

mode_function = calc_mode(houses['Land Slope'])
print(mode_function, '\n')

mode_method = houses['Land Slope'].mode()
print(mode_method, '\n')

same = mode_function == mode_method
print(same)

## 3. The Mode for Nominal Variables ##

def mode(array):
    counts = {}
    
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    return (counts, max(counts, key = counts.get))

value_counts = mode(houses['Roof Style'])[0]
mode = mode(houses['Roof Style'])[1]

print(value_counts)
print(mode)

print(houses['Roof Style'].value_counts())

## 4. The Mode for Discrete Variables ##

print(houses['Bedroom AbvGr'].value_counts(), '\n')
bedroom_variable = 'discrete'

bedroom_mode = houses['Bedroom AbvGr'].mode()
print(bedroom_mode[0], '\n')

print(houses['SalePrice'].value_counts().head(), '\n')
price_variable = 'continuous'


## 5. Special Cases ##

intervals = pd.interval_range(start = 0, end = 800000, freq = 100000)
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0], index = intervals)

for value in houses['SalePrice']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break

print(gr_freq_table, '\n')

interv = gr_freq_table[gr_freq_table == max(gr_freq_table)].index[0]
print(interv, '\n')

mode = int((interv.left + interv.right) / 2)
print('Mode', mode, '\n')

mean = houses['SalePrice'].mean()
print('Mean', mean, '\n')

median = houses['SalePrice'].median()
print('Median', median, '\n')

sentence_1 = True
sentence_2 = True

## 6. Skewed Distributions ##

distribution_1 = {'mean': 3021 , 'median': 3001, 'mode': 2947}
distribution_2 = {'median': 924 , 'mode': 832, 'mean': 962}
distribution_3 = {'mode': 202, 'mean': 143, 'median': 199}

shape_1 = 'right skew'
shape_2 = 'right skew'
shape_3 = 'left skew'

## 7. Symmetrical Distributions ##

houses['Mo Sold'].plot.kde(xlim=(1, 12))
plt.axvline(6, color = 'Green', label = 'Mode')
plt.axvline(houses['Mo Sold'].median(), color = 'Orange', label = 'Median')
plt.axvline(houses['Mo Sold'].mean(), color = 'Black', label = 'Mean')
plt.legend()
plt.show()