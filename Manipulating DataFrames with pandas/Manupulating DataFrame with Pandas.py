# 1 Indexing and column rearrangement
# Import pandas
import pandas as pd 
#print(filename)
# Read in filename and set the index: election
election = pd.read_csv(filename, index_col='county')
print(election.head())
# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = election[['winner', 'total', 'voters']]
# Print the output of results.head()
print(results.head())

# 2 Slicing rows
print(election.head())

#          state   total      Obama     Romney  winner  voters
#county                                                       
#Adams        PA   41973  35.482334  63.112001  Romney   61156
#Allegheny    PA  614671  56.640219  42.185820   Obama  924351
# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election.loc['Perry':'Potter',:]

# Print the p_counties DataFrame
print(p_counties)
#             state   total      Obama     Romney  winner   voters
#county                                                           
#Perry           PA   18240  29.769737  68.591009  Romney    27245
#Philadelphia    PA  653598  85.224251  14.051451   Obama  1099197
# Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev
p_counties_rev = election.loc['Potter':'Perry':-1,:]

# Print the p_counties_rev DataFrame
print(p_counties_rev)
#             state   total      Obama     Romney  winner   voters
#county                                                           
#Potter          PA    7205  26.259542  72.158223  Romney    10913
#Pike            PA   23164  43.904334  54.882576  Romney    41840

# 3: Slicing Columns 
print(election.head())
#           state   total      Obama     Romney  winner  voters
# county                                                       
# Adams        PA   41973  35.482334  63.112001  Romney   61156
# Slice the columns from the starting column to 'Obama': left_columns
left_columns = election.loc[:, :'Obama']

# Print the output of left_columns.head()
print(left_columns.head())
#          state   total      Obama
#county                            
#Adams        PA   41973  35.482334
# Slice the columns from 'Obama' to 'winner': middle_columns
middle_columns = election.loc[:, 'Obama':'winner']

# Print the output of middle_columns.head()
print(middle_columns.head())
#               Obama     Romney  winner
#county                                 
#Adams      35.482334  63.112001  Romney
# Slice the columns from 'Romney' to the end: 'right_columns'
right_columns = election.loc[:, 'Romney':]

# Print the output of right_columns.head()
print(right_columns.head())
#              Romney  winner  voters
#county                              
#Adams      63.112001  Romney   61156

# 4: Subselecting DataFrames with lists
# Create the list of row labels: rows
rows = ['Philadelphia', 'Centre', 'Fulton']

# Create the list of column labels: cols
cols = ['winner', 'Obama', 'Romney']

# Create the new DataFrame: three_counties
three_counties = election.loc[rows,cols]

# Print the three_counties DataFrame
print(three_counties)
#              winner      Obama     Romney
#county                                    
#Philadelphia   Obama  85.224251  14.051451
#Centre        Romney  48.948416  48.977486
#Fulton        Romney  21.096291  77.748861

# 5: Thresholding data
print(election.head(2))
# Create the boolean array: high_turnout
high_turnout = election['turnout'] > 70 

print (high_turnout)
# Filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout_df = election[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)
#             state   total      Obama     Romney  winner  voters    turnout  \
#county                                                                        
#Bucks           PA  319407  49.966970  48.801686   Obama  435606  73.324748   

# 6: Filtering columns using other columns

# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = election['margin'] < 1

# Assign np.nan to the 'winner' column where the results were too close to call
election.loc[too_close, 'winner'] = np.nan

# Print the output of election.info()
print(election.info())

# 7 Filtering using NaNs

# Select the 'age' and 'cabin' columns: df
df = titanic[['age','cabin']]
# Print the shape of df
#print(titanic.head())
print(df.shape)
# (1309, 2)
# Drop rows in df with how='any' and print the shape
print(df.dropna(how='any').shape)
# (272, 2)
# Drop rows in df with how='all' and print the shape
print(df.dropna(how='all').shape)
# (1069, 2)
# Call .dropna() with thresh=1000 and axis='columns' and print the output of .info() from titanic
print(titanic.dropna(thresh=1000, axis='columns').info())

# 8 Transforming DataFrames
# Write a function to convert degrees Fahrenheit to degrees Celsius: to_celsius
def to_celsius(F):
    return 5/9*(F - 32)

# Apply the function over 'Mean TemperatureF' and 'Mean Dew PointF': df_celsius
# print(weather.head())
df_celsius = weather.loc[:,['Mean TemperatureF','Mean Dew PointF']].apply(to_celsius)
# Reassign the columns df_celsius
df_celsius.columns = ['Mean TemperatureC', 'Mean Dew PointC']

# Print the output of df_celsius.head()
print(df_celsius.head())
#     Mean TemperatureC  Mean Dew PointC
#0            -2.222222        -2.777778
#1            -6.111111       -11.111111

#  9. Using .map() with a dictionary
# Create the dictionary: red_vs_blue
red_vs_blue = {'Obama':'blue','Romney':'red'}

# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] = election['winner'].map(red_vs_blue)

# Print the output of election.head()
print(election.head())
#          state   total      Obama     Romney  winner  voters color
#county                                                             
#Adams        PA   41973  35.482334  63.112001  Romney   61156   red
#Allegheny    PA  614671  56.640219  42.185820   Obama  924351  blue
#Armstrong    PA   28322  30.696985  67.901278  Romney   42147   red

# 10. Using vectorized functions

# Import zscore from scipy.stats
from scipy.stats import zscore 

# Call zscore with election['turnout'] as input: turnout_zscore
turnout_zscore = zscore(election['turnout'])

# Print the type of turnout_zscore
print(type(turnout_zscore))
# <class 'numpy.ndarray'>
# Assign turnout_zscore to a new column: election['turnout_zscore']
election['turnout_zscore'] = turnout_zscore

# Print the output of election.head()
print(election.head())
#          state   total      Obama     Romney  winner  voters    turnout  \
#county                                                                     
#Adams        PA   41973  35.482334  63.112001  Romney   61156  68.632677   

# 11. Changing index of a DataFrame
# Create the list of new indexes: new_idx
new_idx = [i.upper() for i in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)

#     eggs  salt  spam
#JAN    47  12.0    17
#FEB   110  50.0    31

# 12. Changing index name labels

print(sales.head(1))
#      eggs  salt  spam
#JAN    47  12.0    17
# Assign the string 'MONTHS' to sales.index.name
sales.index.name = 'MONTHS'

# Print the sales DataFrame
print(sales)
#        eggs  salt  spam
#MONTHS                  
#JAN       47  12.0    17
# Assign the string 'PRODUCTS' to sales.columns.name 
sales.columns.name = 'PRODUCTS'
# Print the sales dataframe again
print(sales)
#PRODUCTS  eggs  salt  spam
#MONTHS                    
#JAN         47  12.0    17

# 13. Building an index, then a DataFrame
# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales.index = months

# Print the modified sales DataFrame
print(sales)
#     eggs  salt  spam
#Jan    47  12.0    17

# 14: Multi index 
# 14.1 Setting & sorting a MultiIndex

# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)
#             eggs  salt  spam
#state month                  
#CA    1        47  12.0    17
#      2       110  50.0    31
#NY    1       221  89.0    72
#      2        77  87.0    20
# 14.2 Using .loc[] with nonunique indexes

print(sales.head())
# Set the index to the column 'state': sales
sales = sales.set_index(['state'])

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY',:])
# state                         
# NY         1   221  89.0    72
# NY         2    77  87.0    20

# 14.3 Indexing multiple levels of a MultiIndex

print(sales.head())
#             eggs  salt  spam
#state month                  
#CA    1        47  12.0    17
#      2       110  50.0    31
#NY    1       221  89.0    72
#      2        77  87.0    20
#TX    1       132   NaN    52
# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[('NY',1),:]
print(NY_month1)
#eggs    221.0
#salt     89.0
#spam     72.0
#Name: (NY, 1), dtype: float64

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA','TX'],2),:]
print(CA_TX_month2)
#             eggs  salt  spam
#state month                  
#CA    2       110  50.0    31
#TX    2       205  60.0    55
# Look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None),2),:]
print(all_month2)
#             eggs  salt  spam
#state month                  
#CA    2       110  50.0    31
#NY    2        77  87.0    20
#TX    2       205  60.0    55

# 14.4 Pivoting DataFrames
# Pivoting a single variable

print(users.head())
#  weekday    city  visitors  signups
#0     Sun  Austin       139        7
#1     Sun  Dallas       237       12
#2     Mon  Austin       326        3
#3     Mon  Dallas       456        5
# Pivot the users DataFrame: visitors_pivot
visitors_pivot = users.pivot(index='weekday', columns='city', values='visitors')

# Print the pivoted DataFrame
print(visitors_pivot)
#city     Austin  Dallas
#weekday                
#Mon         326     456
#Sun         139     237
# Privoting all variables 
print(users.head())
#   weekday    city  visitors  signups
#0     Sun  Austin       139        7
#1     Sun  Dallas       237       12
#2     Mon  Austin       326        3
#3     Mon  Dallas       456        5
# Pivot users with signups indexed by weekday and city: signups_pivot
signups_pivot = users.pivot(index='weekday', columns='city', values='signups')

# Print signups_pivot
print(signups_pivot)
#city     Austin  Dallas
#weekday                
#Mon           3       5
#Sun           7      12
# Pivot users pivoted by both signups and visitors: pivot
pivot = users.pivot(index='weekday', columns='city')

# Print the pivoted DataFrame
print(pivot)
#        visitors        signups       
#city      Austin Dallas  Austin Dallas
#weekday                               
#Mon          326    456       3      5
#Sun          139    237       7     12

# 15 Stacking & unstacking I
print(users.head())
#                visitors  signups
#city   weekday                   
#Austin Mon           326        3
#       Sun           139        7
#Dallas Mon           456        5
#       Sun           237       12
# Unstack users by 'weekday': byweekday
byweekday = users.unstack('weekday')
#        visitors      signups    
#weekday      Mon  Sun     Mon Sun
#city                             
#Austin       326  139       3   7
#Dallas       456  237       5  12
# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level='weekday'))
#                visitors  signups
#city   weekday                   
#Austin Mon           326        3
#       Sun           139        7
#Dallas Mon           456        5
#       Sun           237       12

# 15.1 Restoring the index order
# Stack 'city' back into the index of bycity: newusers
newusers = bycity.stack(level='city')

# Swap the levels of the index of newusers: newusers
newusers = newusers.swaplevel(0, 1)

# Print newusers and verify that the index is not sorted
print(newusers)

# Sort the index of newusers: newusers
newusers = newusers.sort_index()

# Print newusers and verify that the index is now sorted
print(newusers)

# Verify that the new DataFrame is equal to the original
print(newusers.equals(users))


#16 Adding names for readability
print(visitors_by_city_weekday.head())
# Reset the index: visitors_by_city_weekday
visitors_by_city_weekday = visitors_by_city_weekday.reset_index() 

# Print visitors_by_city_weekday
print(visitors_by_city_weekday)

# Melt visitors_by_city_weekday: visitors
visitors = pd.melt(visitors_by_city_weekday, id_vars='weekday', value_name='visitors')

# Print visitors
print(visitors)

# 17 Setting up a pivot table
#print(users.head())
print(users.index)
print(users.columns)
#  weekday    city  visitors  signups
#0     Sun  Austin       139        7
#1     Sun  Dallas       237       12
#2     Mon  Austin       326        3
#3     Mon  Dallas       456        5
# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = users.pivot_table(index='weekday',columns='city' )

# Print by_city_day
print(by_city_day)
#        visitors        signups       
#city      Austin Dallas  Austin Dallas
#weekday                               
#Mon          326    456       3      5
#Sun          139    237       7     12

# 17.1 Using other aggregations in pivot tables

print(users.head())
#  weekday    city  visitors  signups
#0     Sun  Austin       139        7
#1     Sun  Dallas       237       12
#2     Mon  Austin       326        3
#3     Mon  Dallas       456        5
# Use a pivot table to display the count of each column: count_by_weekday1
count_by_weekday1 = pd.pivot_table(users,index='weekday',aggfunc='count')

# Print count_by_weekday
print(count_by_weekday1)
#         city  signups  visitors
#weekday                         
#Mon         2        2         2
#Sun         2        2         2
# Replace 'aggfunc='count'' with 'aggfunc=len': count_by_weekday2
count_by_weekday2 = pd.pivot_table(users,index='weekday',aggfunc=len)

# Verify that the same result is obtained
print('==========================================')
print(count_by_weekday1.equals(count_by_weekday2))
# ==========================================
# True

# 17.2 Using margins in pivot tables
print(users.head())
#  weekday    city  visitors  signups
#0     Sun  Austin       139        7
#1     Sun  Dallas       237       12
#2     Mon  Austin       326        3
#3     Mon  Dallas       456        5
# Create the DataFrame with the appropriate pivot table: signups_and_visitors
signups_and_visitors = pd.pivot_table(users,index='weekday',aggfunc=sum)

# Print signups_and_visitors
print(signups_and_visitors)
print(type(signups_and_visitors))
#         signups  visitors
#weekday                   
#Mon            8       782
#Sun           19       376
# Add in the margins: signups_and_visitors_total 
signups_and_visitors_total = pd.pivot_table(users,index='weekday',margins=True,aggfunc=sum)

# Print signups_and_visitors_total
print(signups_and_visitors_total)
#         signups  visitors
#weekday                   
#Mon          8.0     782.0
#Sun         19.0     376.0
#All         27.0    1158.0

# 18 Group by multi columns 
#print(titanic.head())

# Group titanic by 'pclass'
by_class = titanic.groupby('pclass')

print(by_class.head())
# Aggregate 'survived' column of by_class by count
count_by_class = by_class.survived.count()

# Print count_by_class
print(count_by_class)
#pclass
#1    323
#2    277
#3    709
#Name: survived, dtype: int64

# Group titanic by 'embarked' and 'pclass'
by_mult = titanic.groupby(['embarked','pclass'])

# Aggregate 'survived' column of by_mult by count
count_mult = by_mult.survived.count()

# Print count_mult
print(count_mult)
#embarked  pclass
#C         1         141
#          2          28
#          3         101
#Q         1           3
#          2           7
#          3         113
#S         1         177
#          2         242
#          3         495
#Name: survived, dtype: int64

# 18.1 Grouping by another series
# Read life_fname into a DataFrame: life
life = pd.read_csv(life_fname, index_col='Country')

#print(life.head())
#                      1964    1965    1966    1967    1968    1969    1970  \
#Country                                                                       
#Afghanistan          33.639  34.152  34.662  35.170  35.674  36.172  36.663  
# Read regions_fname into a DataFrame: regions
regions = pd.read_csv(regions_fname, index_col='Country')

#print(life.head())
#                       1964    1965    1966    1967    1968    1969    1970  \
#Country                                                                       
#Afghanistan          33.639  34.152  34.662  35.170  35.674  36.172  36.663 
# Group life by regions['region']: life_by_region
life_by_region = life.groupby(regions['region'])

# Print the mean over the '2010' column of life_by_region
print(life_by_region['2010'].mean())
#region
#America                       74.037350
#East Asia & Pacific           73.405750
#Europe & Central Asia         75.656387
#Middle East & North Africa    72.805333
#South Asia                    68.189750
#Sub-Saharan Africa            57.575080
#Name: 2010, dtype: float64

# 18.2 Computing multiple aggregates of multiple columns
# Group titanic by 'pclass': by_class
by_class = titanic.groupby('pclass')

# Select 'age' and 'fare'
by_class_sub = by_class[['age','fare']]
#      age      fare
#0    29.0  211.3375
#323  30.0   24.0000
#600  42.0    7.5500
# Aggregate by_class_sub by 'max' and 'median': aggregated
aggregated = by_class_sub.agg(['max','median'])

#print(aggregated.head())
#         age             fare         
#         max median       max   median
#pclass                                
#1       80.0   39.0  512.3292  60.0000
# Print the maximum age in each class
print(aggregated.loc[:, ('age','max')])
# pclass
# 1    80.0
# 2    70.0
# 3    74.0
# Name: (age, max), dtype: float64
# Print the median fare in each class
print(aggregated.loc[:, ('fare','median')])
#pclass
#1    60.0000
#2    15.0458
#3     8.0500
#Name: (fare, median), dtype: float64

# 18.3 Aggregating on index levels/fields
# Read the CSV file into a DataFrame and sort the index: gapminder
gapminder = pd.read_csv('gapminder.csv',index_col=['Year','region','Country']).sort_index()

#print(gapminder.head(1))
#                                  fertility    life  population  \
#Year region  Country                                              
#1964 America Antigua and Barbuda       4.25  63.775     58653.0   

# Group gapminder by 'Year' and 'region': by_year_region
by_year_region = gapminder.groupby(level=['Year','region'])
#print(by_year_region.head(1))
#                                                    fertility    life  \
#Year region                     Country                                  
#1964 America                    Antigua and Barbuda      4.250  63.775 
# Define the function to compute spread: spread
def spread(series):
    return series.max() - series.min()

# Create the dictionary: aggregator
aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

# Aggregate by_year_region using the dictionary: aggregated
aggregated = by_year_region.agg(aggregator)

# Print the last 6 entries of aggregated 
print(aggregated.tail(6))
#                                  population  child_mortality       gdp
#Year region                                                             
#2013 America                     9.629087e+08        17.745833   49634.0
#     East Asia & Pacific         2.244209e+09        22.285714  134744.0
#     Europe & Central Asia       8.968788e+08         9.831875   86418.0
#     Middle East & North Africa  4.030504e+08        20.221500  128676.0
#     South Asia                  1.701241e+09        46.287500   11469.0
#     Sub-Saharan Africa          9.205996e+08        76.944490   32035.0


# 18.4 Grouping on a function of the index

# Read file: sales
sales = pd.read_csv('sales.csv',index_col='Date',parse_dates=True)

#print(sales.head(1))
#                    Company   Product  Units
#Date                                        
#2015-02-02 08:30:00   Hooli  Software      3

# Create a groupby object: by_day
by_day = sales.groupby(sales.index.strftime('%a'))

#print(by_day.head(1))
#                             Company   Product  Units
#Date                                                 
#2015-02-02 08:30:00            Hooli  Software      3

# Create sum: units_sum
units_sum = by_day['Units'].sum()

# Print units_sum
print(units_sum)
#Mon    48
#Sat     7
#Thu    59
#Tue    13
#Wed    48
#Name: Units, dtype: int64

# 19 Detecting outliers with Z-Scores
# Import zscore
from scipy.stats import zscore

# Group gapminder_2010: standardized
standardized = gapminder_2010.groupby('region')['life','fertility'].transform(zscore)

# Construct a Boolean Series to identify outliers: outliers
outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)

# Filter gapminder_2010 by the outliers: gm_outliers
gm_outliers = gapminder_2010.loc[outliers]

# Print gm_outliers
print(gm_outliers)
#             fertility    life  population  child_mortality     gdp  \
#Country                                                               
#Guatemala        3.974  71.100  14388929.0             34.5  6849.0  
#                            region  
#Country                             
#Guatemala                  America  

# 20 Filling missing data (imputation) by group
# print(titanic.head(1))
# pclass  survived                           name     sex   age  sibsp  \
#0       1         1  Allen, Miss. Elisabeth Walton  female  29.0      0   

#   parch ticket      fare cabin embarked boat  body     home.dest  
#0      0  24160  211.3375    B5        S    2   NaN  St Louis, MO
# Create a groupby object: by_sex_class
by_sex_class = titanic.groupby(['sex','pclass'])

# Write a function that imputes median
def impute_median(series):
    return series.fillna(series.median())

# Impute age and assign to titanic['age']
titanic.age = by_sex_class.age.transform(impute_median)

# Print the output of titanic.tail(10)
print(titanic.tail(10))

# 20.1 Other transformations with .apply
# Group gapminder_2010 by 'region': regional
regional = gapminder_2010.groupby('region')

# Apply the disparity function on regional: reg_disp
reg_disp = regional.apply(disparity)

# Print the disparity of 'United States', 'United Kingdom', and 'China'
print(reg_disp.loc[['United States','United Kingdom','China']])
#                regional spread(gdp)    z(gdp)
#Country                                       
#United States                47855.0  3.013374
#United Kingdom               89037.0  0.572873
#China                        96993.0 -0.432756

# 21 Grouping and filtering with .apply()
def c_deck_survival(gr):

    c_passengers = gr['cabin'].str.startswith('C').fillna(False)

    return gr.loc[c_passengers, 'survived'].mean()

# Create a groupby object using titanic over the 'sex' column: by_sex
by_sex = titanic.groupby('sex')

# print(by_sex)
# Call by_sex.apply with the function c_deck_survival and print the result
c_surv_by_sex = by_sex.apply(c_deck_survival)

# Print the survival rates
print(c_surv_by_sex)
sex
female    0.913043
male      0.312500
dtype: float64

# 22 Filtering

# Read the CSV file into a DataFrame: sales
sales = pd.read_csv('sales.csv', index_col='Date', parse_dates=True)

print(sales.head(1))
#                    Company   Product  Units
#Date                                        
#2015-02-02 08:30:00   Hooli  Software      3
# Group sales by 'Company': by_company
by_company = sales.groupby('Company')

# Compute the sum of the 'Units' of by_company: by_com_sum
by_com_sum = by_company['Units'].sum()
print(by_com_sum)
#Company
#Acme Coporation    34
#Hooli              30
#Initech            30
#Mediacore          45
#Streeplex          36
#Name: Units, dtype: int64
# Filter 'Units' where the sum is > 35: by_com_filt
by_com_filt = by_company.filter(lambda g:g['Units'].sum() > 35)
print(type(by_com_filt))
print(by_com_filt)
#<class 'pandas.core.frame.DataFrame'>
#                       Company   Product  Units
#Date                                           
#2015-02-02 21:00:00  Mediacore  Hardware      9
#2015-02-04 15:30:00  Streeplex  Software     13
#2015-02-09 09:00:00  Streeplex   Service     19
#2015-02-09 13:00:00  Mediacore  Software      7
#2015-02-19 11:00:00  Mediacore  Hardware     16
#2015-02-19 16:00:00  Mediacore   Service     10
#2015-02-21 05:00:00  Mediacore  Software      3
#2015-02-26 09:00:00  Streeplex   Service      4

# 22.1 Filtering and grouping with .map()

#print(titanic.head(1))
#   pclass  survived                           name     sex   age  sibsp  \
#0       1         1  Allen, Miss. Elisabeth Walton  female  29.0      0   
#
#   parch ticket      fare cabin embarked boat  body     home.dest  
#0      0  24160  211.3375    B5        S    2   NaN  St Louis, MO 
# Create the Boolean Series: under10
under10 = (titanic['age'] < 10).map({True:'under 10', False:'over 10'})

# Group by under10 and compute the survival rate
survived_mean_1 = titanic.groupby(under10)['survived'].mean()
print(survived_mean_1)
#age
#over 10     0.366748
#under 10    0.609756
#Name: survived, dtype: float64
# Group by under10 and pclass and compute the survival rate
survived_mean_2 = titanic.groupby([under10, 'pclass'])['survived'].mean()
print(survived_mean_2)
#age       pclass
#over 10   1         0.617555
#          2         0.380392
#          3         0.238897
#under 10  1         0.750000
#          2         1.000000
#          3         0.446429
#Name: survived, dtype: float64

# 23 Case Study - Summer Olympics
# Redefine 'Medal' as an ordered categorical
# medals.Medal = pd.Categorical(values = medals.Medal,categories=['Bronze', 'Silver', 'Gold'],ordered=True)


# Create the DataFrame: usa
usa = medals[medals['NOC'] == 'USA']
# 
# print(usa)
# Group usa by ['Edition', 'Medal'] and aggregate over 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

# print (usa_medals_by_year)
# Edition  Medal 
# 1896     Bronze      2
#          Gold       11
#         Silver      7
#1900     Bronze     14

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

print(usa_medals_by_year.head(2))
# Medal    Bronze  Gold  Silver
# Edition                      
# 1896          2    11       7
# 1900         14    27      14
# Plot the DataFrame usa_medals_by_year
usa_medals_by_year.plot()
plt.show()

# 24: Visualizing USA Medal Counts by Edition: Area Plot


