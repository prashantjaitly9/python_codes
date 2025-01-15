import numpy as np
# Creating two matrices using NumPy
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])
# Matrix addition
matrix_add = matrix_1 + matrix_2
print("Matrix Addition:\n", matrix_add)
# Matrix multiplication (dot product)
matrix_mul = np.dot(matrix_1, matrix_2)
print("Matrix Multiplication:\n", matrix_mul)
# Transpose of a matrix
transpose_matrix = np.transpose(matrix_1)
print("Transpose of matrix_1:\n", transpose_matrix)