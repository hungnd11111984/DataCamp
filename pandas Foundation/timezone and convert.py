# Buid a Boolean mask to filter out all the 'LAX' departure flights: mask
mask = df['Destination Airport'] == 'LAX'

# Use the mask to subset the data: la
la = df[mask]

# Combine two columns of data to create a datetime series: times_tz_none 
times_tz_none = pd.to_datetime( la['Date (MM/DD/YYYY)'] + ' ' + la['Wheels-off Time'] )
#print(times_tz_none)
#print(type(times_tz_none))
# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')
print(times_tz_central)
print(type(times_tz_central))
# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')
print(times_tz_pacific)

33     2015-07-01 05:43:00-05:00
55     2015-07-01 16:27:00-05:00
91     2015-07-02 05:47:00-05:00
dtype: datetime64[ns, US/Central]
<class 'pandas.core.series.Series'>
1620   2015-07-29 14:29:00-07:00
1656   2015-07-30 03:36:00-07:00
1678   2015-07-30 14:41:00-07:00
dtype: datetime64[ns, US/Pacific]