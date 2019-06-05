## 1. Introduction ##

world_dev = pd.read_csv("World_dev.csv")
col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}

merged = pd.merge(left=happiness2015, right=world_dev, how='left', left_on='Country', right_on='ShortName')

merged = merged.rename(col_renaming, axis=1)
merged.head()

## 2. Using Apply to Transform Strings ##

def extract_last_word(element):
    return str(element).split()[-1]

merged['Currency Apply'] = merged['CurrencyUnit'].apply(extract_last_word)

merged.head()

## 3. Vectorized String Methods Overview ##

merged['Currency Vectorized'] = merged['CurrencyUnit'].str.split().str.get(-1)

print(merged['Currency Vectorized'].head())

## 4. Exploring Missing Values with Vectorized String Methods ##

lengths = merged['CurrencyUnit'].str.len()
value_counts = lengths.value_counts(dropna=False)
value_counts

## 5. Finding Specific Words in Strings ##

pattern = r"[Nn]ational accounts"
national_accounts = merged['SpecialNotes'].str.contains(pattern)

print(national_accounts.head())

## 6. Finding Specific Words in Strings Continued ##

pattern = r"[Nn]ational accounts"
national_accounts = merged['SpecialNotes'].str.contains(r"[Nn]ational accounts", na=False)
merged_national_accounts = merged[national_accounts]

merged_national_accounts.head()

## 7. Extracting Substrings from a Series ##

pattern = r"([1-2][0-9]{3})"

years = merged['SpecialNotes'].str.extract(pattern)
years.head()

## 8. Extracting Substrings from a Series Continued ##

pattern = r"([1-2][0-9]{3})"
years = merged['SpecialNotes'].str.extract(pattern, expand=True)

years.head()

## 9. Extracting All Matches of a Pattern from a Series ##

pattern = r"(?P<Years>[1-2][0-9]{3})"
years = merged['IESurvey'].str.extractall(pattern)

value_counts = years['Years'].value_counts()
print(value_counts)

## 10. Extracting More Than One Group of Patterns from a Series ##

pattern = r"(?P<First_Year>[1-2][0-9]{3})/?(?P<Second_Year>[0-9]{2})?"
years = merged['IESurvey'].str.extractall(pattern)

first_two_year = years['First_Year'].str[0:2]
years['Second_Year'] = first_two_year + years['Second_Year']

years.head()

## 11. Challenge: Clean a String Column, Aggregate the Data, and Plot the Results ##

merged['IncomeGroup'] = merged['IncomeGroup'].str.replace(' income', '').str.replace(':', '').str.upper()

pv_incomes = merged.pivot_table(values='Happiness Score', index='IncomeGroup')

pv_incomes.plot(kind='bar', rot=30, ylim=(0,10))
plt.show()