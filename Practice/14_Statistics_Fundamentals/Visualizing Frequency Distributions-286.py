## 2. Bar Plots ##

wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.bar()
plt.show()

print(wnba['Exp_ordinal'].value_counts())
print(wnba['Exp_ordinal'].head())
print(wnba['Experience'].head())

## 3. Horizontal Bar Plots ##

wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.barh(title = "Number of players in WNBA by level of experience")
plt.show()

## 4. Pie Charts ##

wnba['Exp_ordinal'].value_counts().plot.pie()
#plt.ylabel('')

## 5. Customizing a Pie Chart ##

wnba['Exp_ordinal'].value_counts().plot.pie(
    title='Percentage of players in WNBA by level of experience',
    autopct='%.2f%%', 
    figsize=(6, 6))
plt.ylabel('')
plt.show()

## 6. Histograms ##

wnba['PTS'].plot.hist()
plt.show()

## 7. The Statistics Behind Histograms ##

print(wnba['Games Played'].describe())
wnba['Games Played'].plot.hist()


## 9. Binning for Histograms ##

wnba['Games Played'].plot.hist(range = (1, 32), bins=8, title="The distribution of players by games played")
plt.xlabel('Games played')
plt.show()

## 10. Skewed Distributions ##

assists_distro = 'right skewed'
ft_percent_distro = 'left skewed'

## 11. Symmetrical Distributions ##

normal_distribution = 'Height'