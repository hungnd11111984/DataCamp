# 1 Using .value_counts() for ranking
# print(medals.head(1))
# Select the 'NOC' column of medals: country_names
country_names = medals['NOC']

# Count the number of medals won by each country: medal_counts
medal_counts = country_names.value_counts()

# Print top 15 countries ranked by medals
print(medal_counts.head(15))
#USA    4335
#URS    2049
#GBR    1594
#Name: NOC, dtype: int64

# 2 Using .pivot_table() to count medals by type

# Construct the pivot table: counted
counted = medals.pivot_table(index='NOC', values='Athlete', columns='Medal', aggfunc='count')

# Create the new column: counted['totals']
counted['totals'] = counted.sum(axis='columns')

# Sort counted by the 'totals' column
counted = counted.sort_values('totals', ascending=False)

# Print the top 15 rows of counted
print(counted.head(15))

# 3 Using .pivot_table() to count medals by type
# Construct the pivot table: counted
counted = medals.pivot_table(index='NOC',values='Athlete',columns='Medal',aggfunc='count')

#print(counted)
#Medal  Bronze    Gold  Silver
#NOC                          
#ANZ       5.0    20.0     4.0

# Create the new column: counted['totals']
counted['totals'] = counted.sum(axis='columns')
# print(counted)
# Medal  Bronze    Gold  Silver  totals
# ANZ       5.0    20.0     4.0    29.0

# Sort counted by the 'totals' column
counted = counted.sort_values(by=['totals'], ascending=False)

# Print the top 15 rows of counted
print(counted.head(15))
#Medal  Bronze    Gold  Silver  totals
#NOC                                  
#USA    1052.0  2088.0  1195.0  4335.0
#URS     584.0   838.0   627.0  2049.0

# 4 Applying .drop_duplicates()
# print(medals.head())
# Select columns: ev_gen
ev_gen = medals.loc[:,['Event_gender','Gender']]

# print(ev_gen)
# Drop duplicate pairs: ev_gen_uniques
ev_gen_uniques = ev_gen.drop_duplicates()

# Print ev_gen_uniques
print(ev_gen_uniques)
#      Event_gender Gender
#0                M    Men
#348              X    Men
#416              W  Women
#639              X  Women
#23675            W    Men

# 5 Finding possible errors with .groupby()

# Group medals by the two columns: medals_by_gender
medals_by_gender = medals.groupby(['Event_gender','Gender'])

# Create a DataFrame with a group count: medal_count_by_gender
medal_count_by_gender = medals_by_gender.count()

# Print medal_count_by_gender
print(medal_count_by_gender)
#                     Medal  
#Event_gender Gender         
#M            Men     20067  
#W            Men         1  
#             Women    7277  
#X            Men      1653  
#             Women     218

# 6 Locating suspicious data

# Create the Boolean Series: sus
sus = (medals.Event_gender == 'W') & (medals.Gender == 'Men')

# Create a DataFrame with the suspicious row: suspect
suspect = medals[sus]

# Print suspect
print(suspect)
#         City  Edition      Sport Discipline            Athlete  NOC Gender  \
#23675  Sydney     2000  Athletics  Athletics  CHEPCHUMBA, Joyce  KEN    Men   
#
#          Event Event_gender   Medal  
#23675  marathon            W  Bronze

#7 Using .nunique() to rank by distinct sports

# Group medals by 'NOC': country_grouped
country_grouped = medals.groupby('NOC')

# Compute the number of distinct sports in which each country won medals: Nsports
Nsports = country_grouped['Sport'].nunique()

# Sort the values of Nsports in descending order
Nsports = Nsports.sort_values(ascending=False)

# Print the top 15 rows of Nsports
print(Nsports.head(15))

# 8 Counting USA vs. USSR Cold War Olympic Sports

# Extract all rows for which the 'Edition' is between 1952 & 1988: during_cold_war
during_cold_war = (medals.Edition>=1952) & (medals.Edition<=1988)

# Extract rows for which 'NOC' is either 'USA' or 'URS': is_usa_urs
is_usa_urs = medals.NOC.isin(['USA', 'URS'])

# Use during_cold_war and is_usa_urs to create the DataFrame: cold_war_medals
cold_war_medals = medals.loc[during_cold_war & is_usa_urs]

# Group cold_war_medals by 'NOC'
country_grouped = cold_war_medals.groupby('NOC')

# Create Nsports
Nsports = country_grouped['Sport'].nunique().sort_values(ascending=False)

# Print Nsports
print(Nsports)
#NOC
#URS    21
#USA    20
#Name: Sport, dtype: int64

# 9: Counting USA vs. USSR Cold War Olympic Medals

# print(medals.head(1))
# Create the pivot table: medals_won_by_country
medals_won_by_country = medals.pivot_table(index='Edition',columns='NOC',values='Athlete',aggfunc='count')

# print(medals_won_by_country)
# Slice medals_won_by_country: cold_war_usa_usr_medals
cold_war_usa_usr_medals = medals_won_by_country.loc['1952':'1988', ['USA','URS']]

print(cold_war_usa_usr_medals)
#NOC        USA    URS
#Edition              
#1952     130.0  117.0
#1956     118.0  169.0
# Create most_medals 
most_medals = cold_war_usa_usr_medals.idxmax(axis='columns')

# Print most_medals.value_counts()
print(most_medals.value_counts())
#URS    8
#USA    2
#dtype: int64

# 10: Visualizing USA Medal Counts by Edition: Line Plot


