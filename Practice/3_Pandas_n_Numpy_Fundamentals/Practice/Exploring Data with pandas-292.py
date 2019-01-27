## 2. Using iloc to select by integer position ##

import pandas as pd
import numpy as np

f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

fifth_row = f500.iloc[4]
first_three_rows = f500[:3]
first_seventh_row_slice = f500.iloc[[0, 6], :5]

## 3. Reading CSV files with pandas ##

f500 = pandas.read_csv("f500.csv")
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 4. Working with Integer Labels ##

sorted_emp = f500.sort_values("employees", ascending=False)
top5_emp = sorted_emp.head()

## 5. Using pandas methods to create boolean masks ##

previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["rank"] - previously_ranked["previous_rank"]
print(rank_change)

## 6. Boolean Operators ##

# Example code:
# answer_0 = 1k

answer_1 = 3
answer_2 = 2
answer_3 = 3

## 7. Using Boolean Operators ##

big_rev_neg_profit = f500[(f500["revenues"] > 100000) & (f500["profits"] < 0)]
tech_outside_usa = f500[(f500["sector"] == "Technology") & (~(f500["country"] == "USA"))].head()

print(big_rev_neg_profit)
print(tech_outside_usa)

## 8. Pandas Index Alignment ##

previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["previous_rank"] - previously_ranked["rank"]
f500["rank_change"] = rank_change

## 9. Using Loops with pandas ##

top_employer_by_country = {}
unique_country = f500["country"].unique()

for c in unique_country:
    sorted_companies = f500[f500["country"] == c].sort_values(by="employees", ascending=False)
    employer_row = sorted_companies["company"]
    top_employer = employer_row.iloc[0]
    top_employer_by_country[c] = top_employer
    

    
    

## 10. Challenge: Calculating Return on Assets by Country ##

f500["roa"] = f500["profits"]/f500["assets"]
top_roa_by_sector = {}

companies_by_sector = f500["sector"].unique()

for i in companies_by_sector:
    company_df = f500[f500["sector"] == i].sort_values(by="roa", ascending=False)
    company_series = company_df["company"]
    top_company = company_series.iloc[0]
    top_roa_by_sector[i] = top_company
