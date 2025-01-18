# Use Pandas to modify a DataFrame and compute statistics.
# 1. Create DataFrame: Construct with data:
#         Name: ['Aditi', 'Rahul', 'Deepak', 'Priya', 'Vijay']
#         Age: [25, 30, 35, 40, 45]
#         City: ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Chennai']
# 2. Add Column: Insert 'Age Group' categorizing by age ('20s', '30s', '40s') using pd.cut().
# 3. Filter: Generate a DataFrame for individuals in their 30s.
# 4. Statistics: Calculate and display mean, median, and variance of ages.
# 1. The pandas library must be correctly installed and imported in the script.
# 2. The data for creating the DataFrame must be provided in the exact format and order as listed in the problem description.
# 3. The 'Age Group' column should be correctly inserted using the pd.cut() function and the age groups should be categorized as '20s', '30s' and '40s'.

import numpy as np

np.random.seed(42)

matrix = np.random.rand(5, 5)

print("Original Matrix:")
print(matrix)

# 1. Compute the inverse of the matrix using np.linalg.inv()
try:
    matrix_inv = np.linalg.inv(matrix)
    print("\nInverse of the Matrix:")
    print(matrix_inv)
    
    # 2. Verify the identity matrix using np.allclose() to check if matrix * inverse = identity matrix
    identity_matrix = np.dot(matrix, matrix_inv)
    if np.allclose(identity_matrix, np.eye(5)):
        print("\nThe matrix and its inverse produce the identity matrix.")
    else:
        print("\nThe matrix and its inverse do not produce the identity matrix.")
        
except np.linalg.LinAlgError:
    print("\nThe matrix is singular and cannot be inverted.")

# 3. Calculate statistics for the original matrix
mean_value = np.mean(matrix)
median_value = np.median(matrix)
variance_value = np.var(matrix)

# Round the statistics to at least two decimal places
print("\nStatistics for the Original Matrix:")
print(f"Mean: {np.round(mean_value, 2)}")
print(f"Median: {np.round(median_value, 2)}")
print(f"Variance: {np.round(variance_value, 2)}")
