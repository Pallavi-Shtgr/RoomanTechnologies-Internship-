import numpy as np

# Set a fixed seed for reproducibility
np.random.seed(42)

# Generate a 5x5 matrix with random numbers between 0 and 1
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
