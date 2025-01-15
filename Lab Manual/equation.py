import numpy as np
# Coefficient matrix (A) and the constant terms vector (B)
A = np.array([[6, 2], [5, 5]])
B = np.array([15, 3])
# Solve the system of equations using NumPy's linear algebra module
solution = np.linalg.solve(A, B)
print("Solution for x and y:", solution)