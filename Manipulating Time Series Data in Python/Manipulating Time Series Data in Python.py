# 1 Your first time series

# import pandas as pd
# Create the range of dates here
seven_days = pd.date_range(start='2017-1-1',periods=7)
#DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
#               '2017-01-05', '2017-01-06', '2017-01-07'],
#              dtype='datetime64[ns]', freq='D')
print(seven_days) 
# Iterate over the dates and print the number and name of the weekday
for day in seven_days:
    print(day.dayofweek, day.weekday_name)
#6 Sunday
#0 Monday
#1 Tuesday
#2 Wednesday

# 2 Create a time series of air quality data

# Inspect data
print(data.info())

# Convert the date column to datetime64
data.date = pd.to_datetime(data.date)

# Set date column as index
data.set_index('date', inplace=True)

# Inspect data 
print(data.info())

# Plot data
data.plot(subplots=True)
plt.show()

# 3 Compare annual stock price trends
# Create dataframe prices here
prices = pd.DataFrame()
# print(yahoo.head(1))
#            price
#date             
#2013-01-02  20.08
print (yahoo['2013'])
# Select data for each year and concatenate with prices here 
for year in [yahoo['2013'], yahoo['2014'], yahoo['2015']]:
    price_per_year = yahoo.loc[:, ['price']].reset_index(drop=True)
    price_per_year.rename(columns={'price': year}, inplace=True)
    prices = pd.concat([prices,price_per_year ], axis=1)

# Plot prices
plt.plot(prices)

plt.show()


# 4 Compare annual stock price trends

# Create dataframe prices here
prices = pd.DataFrame()
# print(yahoo.head(1))
#            price
#date             
#2013-01-02  20.08
print (yahoo['2013'].head(2))
# Select data for each year and concatenate with prices here 
for year in ['2013', '2014', '2015']:
    price_per_year = yahoo.loc[year, ['price']].reset_index(drop=True)
    price_per_year.rename(columns={'price': year}, inplace=True)
    prices = pd.concat([prices,price_per_year ], axis=1)

# Plot prices
prices.plot()

plt.show()

# 5 Set and change time series frequency
# Inspect data
print(co.info())
print(co.head(2))
#             Chicago  Los Angeles  New York
#date                                       
#2005-01-01  0.317763     0.777657  0.639830
#2005-01-03  0.520833     0.349547  0.969572
# Set the frequency to calendar daily
co = co.asfreq('D')

print(co.head(10))
# Plot the data
co.plot(subplots=True)
plt.show()

# Set frequency to monthly
co = co.asfreq('M')

print(co.head(10))

# Plot the data
co.plot(subplots=True)

plt.show()

# 6 Shifting stock prices across time

# Import data here
google = pd.read_csv('google.csv', parse_dates=['Date'], index_col='Date')

# Set data frequency to business daily
google = google.asfreq('B')

# Create 'lagged' and 'shifted'
google['shifted'] = google.Close.shift(periods=90)
google['lagged'] = google.Close.shift(periods=-90)

# Plot the google price series
google.plot()
plt.show()

# 7 Calculating stock price changes


# Created shifted_30 here
yahoo['shifted_30'] = yahoo.price.shift(30)

# Subtract shifted_30 from price
yahoo['change_30'] = yahoo.price.sub(yahoo.shifted_30)

# Get the 30-day price difference
yahoo['diff_30'] = yahoo.price.diff(30)

# Inspect the last five rows of price
print(yahoo.tail())
#            price  shifted_30  change_30  diff_30
#date                                             
#2015-12-25    NaN       32.19        NaN      NaN
#2015-12-28  33.60       32.94       0.66     0.66

# Show the value_counts of the difference between change_30 and diff_30
print(yahoo.change_30.sub(yahoo.diff_30).value_counts())

# 8 Plotting multi-period returns

# Create daily_return
google['daily_return'] = google.Close.pct_change().mul(100)

# Create monthly_return
google['monthly_return'] = google.Close.pct_change(30).mul(100)

# Create annual_return
google['annual_return'] = google.Close.pct_change(360).mul(100)

# Plot the result
google.plot(subplots=True)
plt.show()

#9 Compare the performance of several asset classes

# Import data here
prices = pd.read_csv('asset_classes.csv',parse_dates=['DATE'], index_col='DATE')

# Inspect prices here
print(prices.info())

# Select first prices
first_prices = prices.iloc[0]

# Create normalized
normalized = prices.div(first_prices).mul(100)

# Plot normalized
normalized.plot()
plt.show()

# 10 Plot performance difference vs benchmark index

# Create tickers
tickers = ['MSFT','AAPL']
print(type(tickers))

# Import stock data here
stocks = pd.read_csv('msft_aapl.csv',parse_dates=['date'], index_col='date')

# Import index here
sp500 = pd.read_csv('sp500.csv',parse_dates=['date'], index_col='date')

# Concatenate stocks and index here
data = pd.concat([stocks,sp500], axis=1).dropna()

# Normalize data
normalized = normalized = data.div(data.iloc[0]).mul(100)

print(normalized)
# Subtract the normalized index from the normalized stock prices, and plot the result
normalized[tickers].sub(normalized['SP500'],axis=0).plot()
plt.show()
#                  AAPL        MSFT       SP500
#date                                          
#2007-06-29  100.000000  100.000000  100.000000
#2007-07-02   99.368904  100.916186  101.069611

# 11 Convert monthly to weekly data


# Set start and end dates
start = '2016-1-1'
end = '2016-2-29'

# Create monthly_dates here
monthly_dates = pd.date_range(start=start, end=end, freq='M')

# Create monthly here
monthly = pd.Series(data=[1,2], index=monthly_dates)
print(monthly)
# 2016-01-31    1
# 2016-02-29    2
# Create weekly_dates here
weekly_dates = pd.date_range(start=start, end=end, freq='W')

# Print monthly, reindexed using weekly_dates
print(monthly.reindex(weekly_dates))
#Freq: M, dtype: int64
#2016-01-03    NaN
#2016-01-10    NaN
#2016-01-17    NaN
#2016-01-24    NaN
#2016-01-31    1.0
print(monthly.reindex(weekly_dates, method='bfill'))
#Freq: W-SUN, dtype: float64
#2016-01-03    1
#2016-01-10    1
#2016-01-17    1
#2016-01-24    1
#2016-01-31    1
print(monthly.reindex(weekly_dates, method='ffill'))
#Freq: W-SUN, dtype: int64
#2016-01-03    NaN
#2016-01-10    NaN
#2016-01-17    NaN
#2016-01-24    NaN
#2016-01-31    1.0

# 12 Create weekly from monthly unemployment data (Upsampling)
# Inspect data here
print(monthly.info())
print(monthly.index)
# Create weekly dates
weekly_dates = pd.date_range(monthly.index.min(),monthly.index.max(),freq='W')

# Reindex monthly to weekly data
weekly = monthly.reindex(weekly_dates)

# Create ffill and interpolated columns
weekly['ffill'] = weekly.UNRATE.ffill()
weekly['interpolated'] =  weekly.UNRATE.interpolate()

# Plot weekly
weekly.plot()
plt.show()

# 13 Compare weekly, monthly and annual ozone trends for NYC & LA


# Import and inspect data here
ozone = pd.read_csv('ozone.csv', parse_dates=['date'], index_col='date')
ozone.info();

# Calculate and plot the weekly average ozone trend
ozone.resample('W').mean().plot();
plt.show()

# Calculate and plot the monthly average ozone trend
ozone.resample('M').mean().plot();
plt.show();

# Calculate and plot the annual average ozone trend
ozone.resample('A').mean().plot();
plt.show();


# 14 Compare quarterly GDP growth rate and stock returns

# Import and inspect gdp_growth here
gdp_growth = pd.read_csv('gdp_growth.csv', parse_dates=['date'], index_col='date')
gdp_growth.info()

# Import and inspect djia here
djia = pd.read_csv('djia.csv', parse_dates=['date'], index_col='date')
djia.info()

# Calculate djia quarterly returns here 
djia_quarterly = djia.resample('QS').first()
djia_quarterly_return = djia_quarterly.pct_change().mul(100)

# Concatenate, rename and plot djia_quarterly_return and gdp_growth here 
data = pd.concat([gdp_growth, djia_quarterly_return], axis=1)
data.columns = ['gdp', 'djia']

data.plot()
plt.show();


# 15 Visualize monthly mean, median and standard deviation of S&P500 returns
# Import data here
sp500 = pd.read_csv('sp500.csv', parse_dates=['date'], index_col='date')

# Calculate daily returns here
daily_returns = sp500.squeeze().pct_change()

# Resample and calculate statistics
stats = daily_returns.resample('M').agg(['mean', 'median', 'std'])

# Plot stats here
stats.plot()
plt.show();


# 16 Rolling average air quality since 2010 for new york city
# Import and inspect ozone data here
data = pd.read_csv('ozone.csv', parse_dates=['date'], index_col='date').dropna()

# Calculate the rolling mean and std here
rolling_stats = data.rolling('360D').agg(['mean','std'])

# Join rolling_stats with ozone data
stats = data.join(rolling_stats)

# Plot stats
stats.plot(subplots=True)
plt.show()

# 17 Rolling quantiles for daily air quality in nyc

# Resample, interpolate and inspect ozone data here
data = data.resample('D').interpolate()
data.info()

# Create the rolling window
rolling = data.rolling(360)['Ozone']

# Insert the rolling quantiles to the monthly returns
data['q10'] = rolling.quantile(.1)
data['q50'] = rolling.quantile(.5)
data['q90'] = rolling.quantile(.9)

# Plot the data
data.plot()
plt.show()

# 18 Expand Rolling Function for Cumulative 
# Cumulative sum vs .diff()
# Calculate differences
differences = data.diff().dropna()

# Select start price
start_price = data.first('D')

# Calculate cumulative sum
cumulative_sum = start_price.append(differences).cumsum()

# Validate cumulative sum equals data
print(data.equals(cumulative_sum))

# 19 Cumulative return on $1,000 invested in google vs apple I

# Define your investment
investment = 1000

# Calculate the daily returns here
returns = data.pct_change()

# Calculate the cumulative returns here
returns_plus_one = returns.add(1)
cumulative_return = returns_plus_one.cumprod()

# Calculate and plot the investment return here 
cumulative_return.mul(investment).plot()
plt.show();

# 20 Cumulative return on $1,000 invested in google vs apple II
# Import numpy
import numpy as np

# Define a multi_period_return function
def multi_period_return(period_returns):
    return np.prod(period_returns + 1) - 1
    
# Calculate daily returns
daily_returns = data.pct_change()

# Calculate rolling_annual_returns
rolling_annual_returns = daily_returns.rolling('360D').apply(multi_period_return)

# Plot rolling_annual_returns
rolling_annual_returns.mul(100).plot();
plt.show()

# 21 Annual return correlations among several stocks
# Inspect data here

# print(data.head(1))
# Calculate year-end prices here
annual_prices = data.resample('A').last()
print(data.info())
# print(annual_prices)
# Calculate annual returns here
annual_returns = annual_prices.pct_change()

# Calculate and print the correlation matrix here
correlations = annual_returns.corr()
print(correlations)

# Visualize the correlations as heatmap here
sns.heatmap(correlations,annot=True)
plt.show()


# 22 Explore and clean company listing information

# Inspect listings
print(listings.info())

# Move 'stock symbol' into the index
listings.set_index('Stock Symbol', inplace=True)

# Drop rows with missing 'sector' data
listings.dropna(subset=['Sector'], inplace=True)

# Select companies with ipo year before 2019
listings = listings[listings['IPO Year'] < 2019]

# Inspect the new listings data
print(listings.info())

# Show the number of companies per sector
print(listings.groupby('Sector').size().sort_values(ascending=False))


# 23 Select and inspect index components

print(listings.head(1))
# Select largest company for each sector
components = listings.groupby(['Sector'])['Market Capitalization'].nlargest(1)

# Print components, sorted by market cap
print(components.sort_values(ascending=False))

# Select stock symbols and print the result
tickers = components.index.get_level_values('Stock Symbol')
print(tickers)

# Print company name, market cap, and last price for each component 
info_cols = ['Company Name', 'Market Capitalization', 'Last Sale']
print(listings.loc[tickers, info_cols].sort_values('Market Capitalization', ascending=False))


# 24 Import index component price information

# Print tickers
print(tickers)

# Import prices and inspect result
stock_prices = pd.read_csv('stock_prices.csv', parse_dates=['Date'], index_col='Date')
print(stock_prices.info())

# Calculate the returns  
price_return = stock_prices.iloc[-1].div(stock_prices.iloc[0]).sub(1).mul(100)

# Plot horizontal bar chart of sorted price_return   
price_return.sort_values().plot(kind='barh', title='Stock Price Returns')
plt.show()

# 25 Calculate number of shares outstanding

# Inspect listings and print tickers
print(listings.info())
print(tickers)

# Select components and relevant columns from listings
components = listings.loc[tickers, ['Market Capitalization', 'Last Sale']]

# Print the first rows of components
print(components.head())

# Calculate the number of shares here
no_shares = components['Market Capitalization'].div(components['Last Sale'])

# Print the sorted no_shares
print(no_shares.sort_values(ascending=False))

# 26 Create time series of market value


# Select the number of shares
no_shares = components['Number of Shares']
print(no_shares.sort_values())

# Create the series of market cap per ticker
market_cap = stock_prices.mul(no_shares)

# Select first and last market cap here
first_value = market_cap.iloc[0]
last_value = market_cap.iloc[-1]

# Concatenate and plot first and last market cap here
pd.concat([first_value, last_value], axis=1).plot(kind='barh')
plt.show()

# 27 Calculate & plot the composite index
# Aggregate and print the market cap per trading day
raw_index = market_cap_series.sum(axis=1)
print(raw_index)

# Normalize the aggregate market cap here 
index = raw_index.div(raw_index.iloc[0]).mul(100)
print(index)

# Plot the index here
index.plot(title='Market-Cap Weighted Index')
plt.show()


# 28 Calculate the contribution of each stock to the index
# Calculate and print the index return here
index_return = (index.iloc[-1]/index.iloc[0] - 1) * 100
print(index_return)

# Select the market capitalization
market_cap = components['Market Capitalization']

# Calculate the total market cap
total_market_cap = market_cap.sum()

# Calculate the component weights, and print the result
weights = market_cap.div(total_market_cap)
print(weights.sort_values())

# Calculate and plot the contribution by component
weights.mul(index_return).sort_values().plot(kind='barh')
plt.show()

# 29 Compare index performance against benchmark I

# Convert index series to dataframe here
data = index.to_frame('Index')

# Normalize djia series and add as new column to data
djia = djia.div(djia.iloc[0]).mul(100)
data['DJIA'] = djia

# Show total return for both index and djia
print(data.iloc[-1].div(data.iloc[0]).sub(1).mul(100))

# Plot both series
data.plot()
plt.show()

# 30 Compare index performance against benchmark II

# Inspect data
print(data.info())
print(data.head())

# Create multi_period_return function here
def multi_period_return(r):
    return (np.prod(r + 1) - 1) * 100

# Calculate rolling_return_360
rolling_return_360 = data.pct_change().rolling('360D').apply(multi_period_return)

# Plot rolling_return_360 here
rolling_return_360.plot(title='Rolling 360D Return')
plt.show()

# 31 Visualize your index constituent correlations


# Inspect stock_prices here
print(stock_prices.info())

# Calculate the daily returns
returns = stock_prices.pct_change()

# Calculate and print the pairwise correlations
correlations = returns.corr()
print(correlations)

# Plot a heatmap of daily return correlations
sns.heatmap(correlations, annot=True)
plt.title('Daily Return Correlations')
plt.show()

# 32 Save your analysis to multiple excel worksheets


# Inspect index and stock_prices
print(index.info())
print(stock_prices.info())

# Join index to stock_prices, and inspect the result
data = stock_prices.join(index)
print(data.info())

# Create index & stock price returns
returns = data.pct_change()

# export data and data as returns to excel
with pd.ExcelWriter('data.xls') as writer:
    data.to_excel(writer, sheet_name='data')
    returns.to_excel(writer, sheet_name='returns')
    
# 33 







