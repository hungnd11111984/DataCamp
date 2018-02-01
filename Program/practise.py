
# From dict
dict = {
	
"conntry": ["Brazil","Russian","Vietnam"],
"capital": ["Brasilia","Mocow","Hanoi"],
"area": [8.516,17.10,5.34],
"population": [200.4,143.5,100.2]
}

import pandas as pd 

brics = pd.DataFrame(dict)

brics.index = ["BR",'RS','VN']

# FROM CSV

brics = pd.read_csv("path/filesname.csv", index_col = 0)

# Row access = Loc 
iLoc = idex loc 

np.logical_and

# Loop dictionary 
world = { "afghanistan":30.55, 
          "albania":2.77,
          "algeria":39.21 }

for key, value in world.items() :
    print(key + " -- " + str(value))

# Loop numpy 
for x in my_array :

for x in np.nditer(my_array) :

# data Frame 

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Replace the loop above 
cars["COUNTRY"] = cars["country"].apply(str.upper)

