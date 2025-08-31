import numpy as np

# iterate

arr = np.array([[1, 2, 3], [4, 5, 6]])
# normal iteration
for x in arr:
    print(x)

# iterating through each element of the 2-D array
for x in arr:
    for y in x:
        print(y)

# iterating through each element of the 2-D array using nditer()
for x in np.nditer(arr):
    print(x) 



# sorting

arr = np.array([3, 2, 0, 1])
print(arr)
print(np.sort(arr))

alphabet = np.array(['b', 'd', 'a', 'c'])
print(np.sort(alphabet))

bool_arr = np.array([True, False, True])
print(np.sort(bool_arr))

# sorting a 2-D array
arr_2d = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr_2d))  # sorts each row