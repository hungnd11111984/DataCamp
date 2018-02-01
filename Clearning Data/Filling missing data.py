# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality['Ozone'].mean()
print(oz_mean)
# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality.fillna(oz_mean)

# Print the info of airquality
print(airquality.info())


### Result 
44.2209302326
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 153 entries, 0 to 152
Data columns (total 6 columns):
Ozone      153 non-null float64
Solar.R    146 non-null float64
Wind       153 non-null float64
Temp       153 non-null int64
Month      153 non-null int64
Day        153 non-null int64
dtypes: float64(3), int64(3)
memory usage: 7.2 KB
None