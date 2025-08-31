import numpy as np

# shape and reshape

# 1d array
arr1d = np.array([1, 2, 3, 4, 5, 6])
print("1D Array:")
print(arr1d)
print("Shape of 1D array:", arr1d.shape)

# 2d array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr2d)
print("Shape of 2D array:", arr2d.shape)

# Reshape 1d to 2d
reshaped_arr = arr1d.reshape(2, 3)
print("\nReshaped 1D to 2D Array:")
print(reshaped_arr)
print("Shape of reshaped array:", reshaped_arr.shape)

# reshape 1d to 3d
reshaped_arr_3d = arr1d.reshape(2, 1, 3)
print("\nReshaped 1D to 3D Array:")
print(reshaped_arr_3d)
print("Shape of reshaped 3D array:", reshaped_arr_3d.shape)

# flattening arrays
flattened_arr = arr2d.flatten()
print("\nFlattened 2D Array to 1D:")
print(flattened_arr)
print("Shape of flattened array:", flattened_arr.shape)

flattened_arr_3d = reshaped_arr_3d.reshape(-1)
print("\nFlattened 3D Array to 1D:")
print(flattened_arr_3d)
print("Shape of flattened 3D array:", flattened_arr_3d.shape)
