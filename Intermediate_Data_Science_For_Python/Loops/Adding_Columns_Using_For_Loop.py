#Add column (1)

#Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. 
#You can use the string method upper() for this.

_____

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)

_____

#Add column (2)
#Using iterrows() to iterate over every observation of a Pandas DataFrame is easy to understand, but not very efficient. On every iteration, you're creating a new Pandas Series.

#If you want to add a column to a DataFrame by calling a function on another column, the iterrows() method in combination with a for loop is not the preferred way to go. Instead, you'll want to use apply().

#Compare the iterrows() version with the apply() version to get the same result in the brics DataFrame:

for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])

brics["name_length"] = brics["country"].apply(len)
#We can do a similar thing to call the upper() method on every name in the country column. However, upper() is a method, so we'll need a slightly different approach:

#Replace the for loop with a one-liner that uses .apply(str.upper). 
#The call should give the same result: a column COUNTRY should be added to cars, containing an uppercase version of the country names.

_____

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)
