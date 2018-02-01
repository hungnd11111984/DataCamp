# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt,status_country],axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_melt.head())
print(status_country.head())
print(ebola_tidy.head())


(1952, 6)

         Date  Day status_country  counts
0    1/5/2015  289   Cases_Guinea  2776.0
1    1/4/2015  288   Cases_Guinea  2775.0
2    1/3/2015  287   Cases_Guinea  2769.0
3    1/2/2015  286   Cases_Guinea     NaN
4  12/31/2014  284   Cases_Guinea  2730.0
  status country
0  Cases  Guinea
1  Cases  Guinea
2  Cases  Guinea
3  Cases  Guinea
4  Cases  Guinea
         Date  Day status_country  counts status country
0    1/5/2015  289   Cases_Guinea  2776.0  Cases  Guinea
1    1/4/2015  288   Cases_Guinea  2775.0  Cases  Guinea
2    1/3/2015  287   Cases_Guinea  2769.0  Cases  Guinea
3    1/2/2015  286   Cases_Guinea     NaN  Cases  Guinea
4  12/31/2014  284   Cases_Guinea  2730.0  Cases  Guinea