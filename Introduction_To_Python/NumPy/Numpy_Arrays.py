#Baseball player's BMI
#The MLB also offers to let you analyze their weight data. Again, both are available as regular Python lists: height_in and weight. height_in is in inches and weight_lb is in pounds.

#It's now possible to calculate the BMI of each baseball player. Python code to convert height_in to a numpy array with the correct units is already available in the workspace. Follow the instructions step by step and finish the game!

_____

# height and weight are available as regular lists

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb)*0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg/(np_height_m**2)

# Print out bmi
print(bmi)
