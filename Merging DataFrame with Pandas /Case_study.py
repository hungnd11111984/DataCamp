# 1 Loading Olympic edition DataFrame


#Import pandas
import pandas as pd

# Create file path: file_path
file_path = 'Summer Olympic medallists 1896 to 2008 - EDITIONS.tsv'

# Load DataFrame from file_path: editions
editions = pd.read_csv(file_path,sep='\t')

# Extract the relevant columns: editions
editions = editions[['Edition','Grand Total', 'City', 'Country']]

# Print editions DataFrame
print(editions)
#    Edition  Bronze  Gold  Silver  Grand Total         City  Country
#0      1896      40    64      47          151       Athens  Greece

# 2 Loading IOC codes DataFrame
# Import pandas
import pandas as pd

# Create the file path: file_path
file_path = 'Summer Olympic medallists 1896 to 2008 - IOC COUNTRY CODES.csv'

# Load DataFrame from file_path: ioc_codes
ioc_codes = pd.read_csv(file_path)

# Extract the relevant columns: ioc_codes
ioc_codes = ioc_codes[['Country' , 'NOC']]

# Print first and last 5 rows of ioc_codes
print(ioc_codes.head(5))
print(ioc_codes.tail(5))
#           Country  NOC
#0      Afghanistan  AFG
#200         Zimbabwe  ZIM

# 3 Building medals DataFrame
# Import pandas
import pandas as pd

# Create empty dictionary: medals_dict
medals_dict = {}

for year in editions['Edition']:

    # Create the file path: file_path
    file_path = 'summer_{:d}.csv'.format(year)
    
    # Load file_path into a DataFrame: medals_dict[year]
    medals_dict[year] = pd.read_csv(file_path)
    
    # Extract relevant columns: medals_dict[year]
    medals_dict[year] = medals_dict[year][['Athlete', 'NOC', 'Medal']]
    
    # Assign year to column 'Edition' of medals_dict
    medals_dict[year]['Edition'] = year
    
# Concatenate medals_dict: medals
medals = pd.concat(medals_dict,ignore_index=True)

# Print first and last 5 rows of medals
print(medals.head())
print(medals.tail())
#              Athlete  NOC   Medal  Edition
#0       HAJOS, Alfred  HUN    Gold     1896
#29215        BAROEV, Khasan  RUS  Silver     2008

# 4 Counting medals by country/edition in a pivot table

# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(index='Edition',values='Athlete',columns='NOC',aggfunc='count')

# Print the first & last 5 rows of medal_counts
print(medal_counts.head())
print(medal_counts.tail())
# NOC      AFG  AHO  ALG  ANZ   ARG  ARM    AUS  AUT  AZE  BAH ...   URS  URU  \
# Edition                                                      ...              
# 1992     NaN  NaN  2.0  NaN   2.0  NaN   57.0  6.0  NaN  1.0 ...   NaN  NaN   

# 5 Computing fraction of medals per Olympic edition
print(editions.head(1))
#   Edition  Grand Total    City Country
#0     1896          151  Athens  Greece
# Set Index of editions: totals
totals = editions.set_index('Edition')
print(totals.head(1))
#         Grand Total    City Country
#Edition                             
#1896             151  Athens  Greece
# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']

print(totals)
# Divide medal_counts by totals: fractions
fractions = medal_counts.divide(totals,axis='rows')

# Print first & last 5 rows of fractions
print(fractions.head())
print(fractions.tail())
#NOC      AFG  AHO  ALG       ANZ  ARG  ARM       AUS       AUT  AZE  BAH  \
#Edition                                                                    
#1896     NaN  NaN  NaN       NaN  NaN  NaN  0.013245  0.033113  NaN  NaN 

# 6 Computing percentage change in fraction of medals won
# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()

print(mean_fractions)
#NOC          AFG       AHO       ALG       ANZ       ARG       ARM       AUS  \
#Edition                                                                        
#1896         NaN       NaN       NaN       NaN       NaN       NaN  0.013245 
# Compute the percentage change: fractions_change
fractions_change = mean_fractions.pct_change() * 100 

# Reset the index of fractions_change: fractions_change
fractions_change = fractions_change.reset_index()

# Print first & last 5 rows of fractions_change
print(fractions_change.head())
print(fractions_change.tail())
#NOC  Edition  AFG  AHO        ALG  ANZ       ARG        ARM        AUS  \
#21      1992  NaN  0.0  -7.214076  0.0 -6.767308        NaN   2.754114 

# 7 Building hosts DataFrame

# Import pandas
import pandas as pd

# Left join editions and ioc_codes: hosts
hosts = pd.merge(editions,ioc_codes, how='left')
#print(editions.head(1))
#print(ioc_codes.head(1))

# Extract relevant columns and set index: hosts
hosts = hosts[['Edition', 'NOC']].set_index('Edition')

print(hosts)
# Fix missing 'NOC' values of hosts
print(hosts.loc[hosts.NOC.isnull()])
hosts.loc[1972, 'NOC'] = 'FRG'
hosts.loc[1980, 'NOC'] = 'URS'
hosts.loc[1988, 'NOC'] = 'KOR'

# Reset Index of hosts: hosts
hosts = hosts.reset_index()

# Print hosts
print(hosts)
#    Edition  NOC
#0      1896  GRE

# 8 Reshaping for analysis

print(fractions_change.head(1))
# NOC  Edition  AFG  AHO  ALG  ANZ  ARG  ARM  AUS  AUT  AZE ...   URS  URU  USA  \
# 0       1896  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN ...   NaN  NaN  NaN   
# Import pandas
import pandas as pd

# Reshape fractions_change: reshaped
reshaped = pd.melt(fractions_change,id_vars='Edition',value_name='Change')
print(reshaped.head(1))
#   Edition  NOC  value
#0     1896  AFG    NaN

# Print reshaped.shape and fractions_change.shape
print(reshaped.shape, fractions_change.shape)
# (3614, 2) (26, 139)
# Extract rows from reshaped where 'NOC' == 'CHN': chn
chn = reshaped[reshaped['NOC'] == 'CHN']

# Print last 5 rows of chn with .tail()
print(chn.tail())
#     NOC      value
#593  CHN   4.240630

# 9: Merging to compute influence
# Import pandas
import pandas as pd

# Merge reshaped and hosts: merged
merged = pd.merge(reshaped,hosts)

# Print first 5 rows of merged
print(merged.head(5))
#   Edition  NOC     Change
#0     1956  AUS  54.615063
# Set Index of merged and sort it: influence
influence = merged.set_index('Edition').sort_index()

# Print first 5 rows of influence
print(influence.head(5))
#         NOC      Change
#Edition                 
#1896     GRE         NaN
#1900     FRA  198.002486

# 10: Plotting influence of host country

# Import pyplot
import matplotlib.pyplot as plt

# Extract influence['Change']: change
change = influence['Change']

# Make bar plot of change: ax
ax = change.plot(kind='bar')

# Customize the plot to improve readability
ax.set_ylabel("% Change of Host Country Medal Count")
ax.set_title("Is there a Host Country Advantage?")
ax.set_xticklabels(editions['City'])

# Display the plot
plt.show()


