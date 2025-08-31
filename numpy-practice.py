import numpy as np

# copy vs view
arr = np.array([1, 2, 3, 4, 5])
arr_copy = arr.copy()
arr_view = arr.view()

arr[0] = 10
print("Original array:", arr)
print("Copy of array:", arr_copy)
print("View of array:", arr_view)

# change in view reflects in original
arr_view[1] = 20
print("After modifying view:")
print("Original array:", arr)
print("View of array:", arr_view)
