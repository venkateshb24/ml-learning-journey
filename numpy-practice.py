import numpy as np

# searching for a value in a 1D array

# using np.where
arr = np.array([10, 20, 30, 40, 50, 30])
index = np.where(arr == 30)
print("Index of 30 using np.where:", index)  # Output: (array([2, 5]),)

# only even numbers in a 1D array using where
even_indices = np.where(arr % 2 == 0)
print("Indices of even numbers using np.where:", even_indices[0])  # Output: [0 1 2 3 4]

# filtering using boolean indexing
even_numbers = arr[arr % 2 == 0]
print("Even numbers using boolean indexing:", even_numbers)  # Output: [10 20 30 40 50 30]

