# 1 Reading DataFrames from multiple files in a loop

# Import pandas
import pandas as pd

# Create the list of file names: filenames
filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']

# Create the list of three DataFrames: dataframes
dataframes = []
for filename in filenames:
    dataframes.append(pd.read_csv(filename))

# Print top 5 rows of 1st DataFrame in dataframes
print(dataframes[0].head())

# 2 Combining DataFrames from multiple data files
# Import pandas
import pandas as pd

# Make a copy of gold: medals
medals = gold.copy()

# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']

# Rename the columns of medals using new_labels
medals.columns = new_labels

# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver['Total']
medals['Bronze'] = bronze['Total']

# Print the head of medals
print(medals.head())
#   NOC         Country    Gold  Silver  Bronze
#0  USA   United States  2088.0  1195.0  1052.0

# 3 Sorting DataFrame with the Index & columns
# Import pandas
import pandas as pd

# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv('monthly_max_temp.csv', index_col='Month')

# Print the head of weather1
print(weather1.head())
#        Max TemperatureF
# Month                  
# Jan                  68
# Feb                  60
# Mar                  68

# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()

# Print the head of weather2
print(weather2.head())
#        Max TemperatureF
# Month                  
# Apr                  84
# Aug                  86
# Dec                  68

# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather1.sort_index(ascending=False)

# Print the head of weather3
print(weather3.head())
#        Max TemperatureF
# Month                  
# Sep                  90
# Oct                  84
# Nov                  72
# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values('Max TemperatureF') 

# Print the head of weather4
print(weather4.head())
#        Max TemperatureF
# Month                  
# Feb                  60
# Jan                  68
# Mar                  68

# 4 Reindexing DataFrame from a list

# Import pandas
import pandas as pd

# print(year)
# Reindex weather1 using the list year: weather2
weather2 = weather1.reindex(year)

# Print weather2
print(weather2)
#       Mean TemperatureF
#Month                   
#Jan            32.133333
#Feb                  NaN
# Reindex weather1 using the list year with forward-fill: weather3
weather3 = weather1.reindex().ffill()

# Print weather3
print(weather3)
#       Mean TemperatureF
#Month                   
#Jan            32.133333
#Feb            32.133333
#Mar            32.133333
#Apr            61.956044
#May            61.956044

# 5 Computing percentage growth of GDP

import pandas as pd

# Read 'GDP.csv' into a DataFrame: gdp
gdp = pd.read_csv('GDP.csv',parse_dates=True,index_col='DATE')

#print(gdp.head(2))
#            VALUE
#DATE             
#1947-01-01  243.1
#1947-04-01  246.3
# Slice all the gdp data from 2008 onward: post2008
post2008 = gdp['2008':]

# Print the last 8 rows of post2008
print(post2008.tail(8))

# Resample post2008 by year, keeping last(): yearly
yearly = post2008.resample('A').last()

# Print yearly
print(yearly)

# Compute percentage growth of yearly: yearly['growth']
yearly['growth'] = yearly.pct_change() * 10

# Print yearly again
print(yearly)
#              VALUE    growth
#DATE                         
#2008-12-31  14549.9       NaN
#2009-12-31  14566.5  0.011409
#2010-12-31  15230.2  0.455635

# 6 Converting currency of stocks

# Import pandas
import pandas as pd

# Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv('sp500.csv',parse_dates=True,index_col='Date')

# print(sp500.head(1))
#                    Open         High          Low        Close      Volume  \
# Date                                                                         
# 2015-01-02  2058.899902  2072.360107  2046.040039  2058.199951  270870000
# Read 'exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv('exchange.csv',parse_dates=True,index_col='Date')
# print(exchange.head(1))
#             GBP/USD
# Date               
# 2015-01-02  0.65101
# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500[['Open','Close']]

# Print the head of dollars
print(dollars.head())
#                    Open        Close
# Date                                
# 2015-01-02  2058.899902  2058.199951

# Convert dollars to pounds: pounds
pounds = dollars.multiply(exchange['GBP/USD'],axis='rows')

# Print the head of pounds
print(pounds.head())
#                   Open        Close
#Date                                
#2015-01-02  1340.364425  1339.908750



