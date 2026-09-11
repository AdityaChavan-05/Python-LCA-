# Program to add two matrices using arrays

import numpy as np

# Function to add two matrices
def add_matrices(mat1, mat2):
    if mat1.shape != mat2.shape:
        print("Error: Matrices must have the same dimensions to add.")
        return None
    return mat1 + mat2

# Accept matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter elements of first matrix:")
mat1 = np.array([[int(input(f"Element [{i+1},{j+1}] : ")) for j in range(cols)] for i in range(rows)])

print("\nEnter elements of second matrix:")
mat2 = np.array([[int(input(f"Element [{i+1},{j+1}] : ")) for j in range(cols)] for i in range(rows)])

# Perform addition
result = add_matrices(mat1, mat2)

# Display results
print("\nFirst Matrix:\n", mat1)
print("\nSecond Matrix:\n", mat2)
print("\nResultant Matrix after Addition:\n", result)
