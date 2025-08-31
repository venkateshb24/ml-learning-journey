import numpy as np

# slicing a 1D array

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])  # Output: [2 3 4 5]

# returning till end of array
print(arr[4:])  # Output: [5 6 7]

# return negative index
print(arr[-3: -1])  # Output: [5 6]

# steps
print(arr[1:6])
print(arr[1:6:2])  # Output: [2 4 6]

# steps on entire array
print(arr[::2])  # Output: [1 3 5 7]
print(arr[::3]) # Output: [1 4 7]

# slice a 2D array
arr2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# pull out a single element
print(arr2d[1,3])  # Output: 9

#slice
print(arr2d[0:1,1:3])  # Output: [[2 3]]
print(arr2d[0:2,1:3])  # Output: [[2 3] [7 8]]

