# 1 Zip lists to build a DataFrame
# Display tuple
print(list_keys)
# ['Country', 'Total']
print(list_values)
# [['United States', 'Soviet Union', 'United Kingdom'], [1118, 473, 273]]
# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys,list_values))

# Inspect the list using print()
print(zipped)
# [('Country', ['United States', 'Soviet Union', 'United Kingdom']), ('Total', [1118, 473, 273])]

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)
#          Country  Total
#0   United States   1118
#1    Soviet Union    473
#2  United Kingdom    273


# 2 Building DataFrames with broadcasting
# Make a string with the value 'PA': state
state = 'PA'
# print cities list
print(cities)
# ['Manheim', 'Preston park', 'Biglerville', 'Indiana', 'Curwensville', 'Crown', 'Harveys lake', 'Mineral springs', 'Cassville', 'Hannastown', 'Saltsburg', 'Tunkhannock', 'Pittsburgh', 'Lemasters', 'Great bend'

# Construct a dictionary: data
data = {'state':state, 'city':cities}

# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
#               city state
#0           Manheim    PA
#1      Preston park    PA
#2       Biglerville    PA
#3           Indiana    PA
#4      Curwensville    PA

# 3: Import / Export Data 
# 3.1 Reading Flat File 
# Read in the file: df1
df1 = pd.read_csv('world_population.csv')

# Create a list of the new column labels: new_labels
new_labels = ['year','population']

# Read in the file, specifying the header and names parameters: df2
df2 = pd.read_csv('world_population.csv', header=0, names=new_labels)

# Print both the DataFrames
print(df1)
#   Year  Total Population
#0  1960      3.034971e+09
#1  1970      3.684823e+09
print(df2)
#   year    population
#0  1960  3.034971e+09
#1  1970  3.684823e+09

# 3.2 Delimiters, headers, and extensions
# print(file_messy)
# messy_stock_data.tsv
# Read the raw file as-is: df1
df1 = pd.read_csv(file_messy)

# Print the output of df1.head()
print(df1.head())
# ....
# ....
# IBM 156.08 160.01 159.81 165.22 172.25 167.15 1...                                                NaN                        
#     name     Jan     Feb     Mar     Apr     May     Jun     Jul     Aug  \
#0     IBM  156.08  160.01  159.81  165.22  172.25  167.15  164.75  152.77 
# Read in the file with the correct parameters: df2
df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')

# Print the output of df2.head()
print(df2.head())
#      Sep     Oct     Nov     Dec  
#0  145.36  146.11  137.21  137.96  
#1   43.56   48.70   53.88   55.40 
# Save the cleaned up DataFrame to a CSV file without the index
df2.to_csv(file_clean, index=False)

# Save the cleaned up DataFrame to an excel file without the index
df2.to_excel('file_clean.xlsx', index=False)

# 
