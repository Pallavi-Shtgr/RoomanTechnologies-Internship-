"""Day 05 MODULES AND LIBRARIES """

# Create a NumPy array [1, 2, 3, 4, 5].
# Add 10 to each element in the array.
# Calculate and return the mean of the original array.
# The function should return a dictionary with the modified array and the mean.

import numpy as np
def numpy_operations()-> dict:
   original_array= np.array([1,2,3,4,5])

   modified_array=original_array+10

   mean_value=np.mean(original_array)

   return{
    'modified_array':modified_array,
    'mean':mean_value
   }
    

