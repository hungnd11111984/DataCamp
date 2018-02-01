# Melt tb: tb_melt
tb_melt = pd.melt(tb, id_vars=['country', 'year'])

print(tb_melt.head())

# Create the 'gender' column
tb_melt['gender'] = tb_melt.variable.str[0]

# Create the 'age_group' column
tb_melt['age_group'] = tb_melt.variable.str[1:4]

# Print the head of tb_melt
print(tb_melt.head())


### Result ### 
<script.py> output:
      country  year variable  value
    0      AD  2000     m014    0.0
    1      AE  2000     m014    2.0
    2      AF  2000     m014   52.0
    3      AG  2000     m014    0.0
    4      AL  2000     m014    2.0
      country  year variable  value gender age_group
    0      AD  2000     m014    0.0      m       014
    1      AE  2000     m014    2.0      m       014
    2      AF  2000     m014   52.0      m       014
    3      AG  2000     m014    0.0      m       014
    4      AL  2000     m014    2.0      m       014