## 3. Condensing the Class Size Data Set ##

class_size = data['class_size']
class_size = class_size[class_size['GRADE '] == '09-12']
class_size = class_size[class_size['PROGRAM TYPE'] == 'GEN ED']
class_size.head(3)

## 5. Computing Average Class Sizes ##

import numpy as np

class_size = class_size.groupby('DBN').agg(np.mean)

class_size.reset_index(inplace=True)

data['class_size'] = class_size

# Grouping the DataFrame using groupby method
# nn = class_size.groupby('DBN')

# Printing the groupby object
# for k,v in nn:
#     print(nn.get_group(k).head(3), "\n\n")
# nn.describe()

class_size.head(3)

## 7. Condensing the Demographics Data Set ##

demographics = data['demographics']
demographics = demographics[demographics['schoolyear']==20112012]

data['demographics'] = demographics
data['demographics'].head()

## 9. Condensing the Graduation Data Set ##

graduation = data['graduation']
graduation = graduation[graduation['Cohort'] == '2006']
graduation = graduation[graduation['Demographic'] == 'Total Cohort']

data['graduation'] = graduation
data['graduation'].head(3)

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

for item in cols:
    data['ap_2010'][item] = pd.to_numeric(data['ap_2010'][item], errors='coerce')
    
data['ap_2010'].dtypes

## 12. Performing the Left Joins ##

combined = data['sat_results']

combined = combined.merge(data['ap_2010'], on='DBN', how='left')
combined = combined.merge(data['graduation'], on='DBN', how='left')
print(combined.shape)
combined.head(3)

## 13. Performing the Inner Joins ##

combined = combined.merge(data['class_size'], on='DBN', how='inner')
combined = combined.merge(data['demographics'], on='DBN', how='inner')
combined = combined.merge(data['survey'], on='DBN', how='inner')
combined = combined.merge(data['hs_directory'], on='DBN', how='inner')

print(combined.shape)
combined.head(3)

## 15. Filling in Missing Values ##

means = combined.mean()
combined = combined.fillna(means)
combined = combined.fillna(0)
combined.head(3)

## 16. Adding a School District Column for Mapping ##

def first_two(a):
    return a[:2]

combined['school_dist'] = combined['DBN'].apply(first_two)
combined['school_dist'].head()