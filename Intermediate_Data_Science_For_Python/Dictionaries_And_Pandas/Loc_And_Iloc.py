#loc and iloc (1)

#With loc and iloc you can do practically any data selection operation on DataFrames you can think of. loc is label-based, which means that you have to specify rows and columns based on their row and column labels. 

#iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.

In [1]: cars
Out[1]: 
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JAP           588          Japan         False
IN             18          India         False
RU            200         Russia          True
MOR            70        Morocco          True
EG             45          Egypt          True

#Use loc or iloc to select the observation corresponding to Japan as a Series. The label of this row is JAP, the index is 2. Make sure to print the resulting Series.

#Use loc or iloc to select the observations for Australia and Egypt as a DataFrame. You can find out about the labels/indexes of these rows by inspecting cars in the IPython Shell. Make sure to print the resulting DataFrame.
_____

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JAP'])

# Print out observations for Australia and Egypt
print(cars.iloc[[1,6]])

_____

#loc and iloc (2)

#loc and iloc also allow you to select both rows and columns from a DataFrame.

#Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)

#Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.
_____

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR','drives_right'])

# Print sub-DataFrame
print(cars.iloc[[4,5],[1,2]])

_____

#loc and iloc (3)

#It's also possible to select only columns with loc and iloc. In both cases, you simply put a slice going from beginning to end in front of the comma:

cars.loc[:, 'country']
cars.iloc[:, 1]

cars.loc[:, ['country','drives_right']]
cars.iloc[:, [1, 2]]

#Print out the drives_right column as a Series using loc or iloc.

#Print out the drives_right column as a DataFrame using loc or iloc.

#Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc.

_____

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.iloc[:,[2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.iloc[:,[0,2]])
