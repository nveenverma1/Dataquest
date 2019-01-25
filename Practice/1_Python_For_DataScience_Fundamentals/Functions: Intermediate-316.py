## 1. Interfering with the Built-in Functions ##

a_list = [1, 8, 10, 9, 7]

max_value = max(a_list)
print(max_value)

def max(a_list1):
    return "This function doesn't return the maximum value"

del max
max_val_test_0 = max(a_list)
print(max_val_test_0)

#max = 100
max_value_test_1 = max(a_list)
print(max_value_test_1)



## 2. Default Arguments ##

def open_dataset(a = 'AppleStore.csv'):
    opened_file = open(a)
    from csv import reader
    read_file = reader(opened_file)
    return list(read_file)

apps_data = open_dataset()

## 3. The Official Python Documentation ##

one_decimal = round(3.43, 1)
two_decimals = round(0.23321, 2)
five_decimals = round(921.2225227, 5)

## 4. Multiple Return Statements ##

def open_dataset(file_name='AppleStore.csv', has_headers = True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if has_headers:
        return data[1:]
    
    return data

apps_data = open_dataset()

## 5. Returning Multiple Variables ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    head = data[0]
    
    if header:
        return head, data[1:]
    else:
        return data
    
all_data = open_dataset()
header = all_data[0]
apps_data = all_data[1]

## 6. More About Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
    
apps_data, header = open_dataset()

## 7. Functions — Code Running Quirks ##

def print_constant():
    x = 3.14
    print(x)
    
print_constant()
#print(x)

## 8. Scopes — Global and Local ##

e = 'mathematical constant'
a_sum = 1000
length = 50

def exponential(x):
    e = 2.72
    print(e)
    return e**x

result = exponential(5)
print(e)

def divide():
    print(a_sum)
    print(length)
    return a_sum/length

result_2 = divide()

## 9. Scopes — Searching Order ##

def open_iOS_dataset():        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    global apps_data
    apps_data = data[1:]
    global header_row
    header_row = data[0]
    
file_name = 'AppleStore.csv'
open_iOS_dataset()
print(header_row)
first_five = apps_data[:5]

## 10. Functions — More Quirks ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
def relative_freqs(table):
    sum1 = 0
    for i in table:
        sum1 += table[i]
    for i in table:
        table[i] = (table[i]/sum1) * 100
        
    return table

c_ratings_percentages = relative_freqs(content_ratings)
print(content_ratings)
changed = True
        

## 11. Mutable and Immutable Types ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

def relative_freqs(freq_table):
    total = 0 
    freq_table1 = freq_table.copy()
    for key in freq_table1:
        count = freq_table1[key]
        total += count
    
    for key in freq_table1:
        freq_table1[key] = (freq_table1[key] / total) * 100
    
    return freq_table1

relative_freqs(content_ratings)
print(content_ratings)
changed = False