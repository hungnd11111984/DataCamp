# Convert 'total_bill' to a numeric dtype
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')

# Convert 'tip' to a numeric dtype
tips['tip'] = pd.to_numeric(tips['tip'], errors='coerce')

# Print the info of tips
print(tips.info())
print(tips)


<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 7 columns):
total_bill    202 non-null float64
tip           220 non-null float64
sex           234 non-null category
smoker        229 non-null category
day           243 non-null category
time          227 non-null category
size          231 non-null float64
dtypes: category(4), float64(3)
memory usage: 6.9 KB
None
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner   2.0
1       10.34  1.66    Male     No  Sun  Dinner   NaN
2       21.01  3.50    Male     No  Sun  Dinner   NaN
3         NaN  3.31    Male     No  Sun  Dinner   2.0