
# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(xl.sheet_names[1])

# Print the head of the DataFrame df2
df2 = xl.parse(0)
# df2 = xl.parse(xl.sheet_names[0]) -- Same result.
