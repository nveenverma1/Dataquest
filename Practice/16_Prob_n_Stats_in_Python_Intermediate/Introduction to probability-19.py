## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])

most_bars = max(flags['bars'])
most_bars_country = flags[flags['bars'] == most_bars]['name']
print(most_bars_country)

highest_population = flags['population'].max()
highest_population_country = flags[flags['population'] == highest_population]['name']     

print(flags.shape)
print(flags.columns)

## 2. Calculating probability ##

total_countries = flags.shape[0]

orange_flags = flags[flags['orange']==1]
print(orange_flags.shape[0])

orange_probability = orange_flags.shape[0]/total_countries
print(orange_probability, '\n')

stripes_flags = flags[flags['stripes'] > 1]
print(stripes_flags.shape[0])

stripe_probability = stripes_flags.shape[0]/total_countries
print(stripe_probability)

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5

ten_heads = .5 ** 10
hundred_heads = .5 ** 100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
red_flags = flags[flags['red'] == 1].shape[0]
print(red_flags)

three_red = (red_flags/total_countries) * (red_flags-1)/(total_countries-1) * (red_flags-2)/(total_countries-2)
print(three_red)

## 5. Disjunctive probability ##

start = 1
end = 18000

def calc_evenly_divisible(start, end, value):
    divisibles = 0
    
    for i in range(start, end+1):
        if (i % value == 0):
            divisibles += 1
    return divisibles

hundred_prob = calc_evenly_divisible(start, end, 100)/end
seventy_prob = calc_evenly_divisible(start, end, 70)/end

print(hundred_prob)
print(seventy_prob)

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None
total_countries = flags.shape[0]

orange_prob = flags[flags['orange']==1].shape[0]/total_countries
print(orange_prob)

red_prob = flags[flags['red']==1].shape[0]/total_countries
print(red_prob)

red_n_orange_prob = flags[(flags['red'] == 1) & (flags['orange'] == 1)].shape[0]/total_countries
print(red_n_orange_prob)

red_or_orange = red_prob + orange_prob - red_n_orange_prob
print(red_or_orange, '\n')

stripe_prob = flags[flags['stripes'] >= 1].shape[0]/total_countries
print(stripe_prob)

bars_prob = flags[flags['bars'] >= 1].shape[0]/total_countries
print(bars_prob)

stripes_n_bars_prob = flags[(flags['stripes'] >= 1) & (flags['bars'] >= 1)].shape[0]/total_countries
print(stripes_n_bars_prob)

stripes_or_bars = stripe_prob + bars_prob - stripes_n_bars_prob
print(stripes_or_bars)

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None

all_three_tails = 0.5*0.5*0.5

heads_or = 1 - all_three_tails
print(heads_or)