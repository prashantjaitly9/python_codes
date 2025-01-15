# import numpy as np
# # Creating a 1D NumPy array
# arr = np.array([10, 20, 30, 40, 50])
# # Basic Array Operations
# print("Array:", arr)
# print("Array Shape:", arr.shape)
# print("Sum of elements:", np.sum(arr))
# print("Mean of elements:", np.mean(arr))
# # Reshaping the array into a 2D array
# arr_2d = arr.reshape(5, 1)
# print("Reshaped to 2D:\n", arr_2d)



import numpy as np
# Create two arrays of different shapes
A = np.array([[1, 2, 3], [4, 5, 6]]) # 2x3 array
B = np.array([10, 20, 30]) # 1D array of size 3
# Broadcasting: adding a 1D array to a 2D array
C = A + B
print("Broadcasted Addition:\n", C)
# Element-wise operations
D = A * 2
print("Element-wise multiplication by 2:\n", D)