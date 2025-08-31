# we already have list but it won't be work good for larger datasets
# for larger datasets we can use numpy arrays

import numpy as np

# numpy - numerical python
# n-d array - multidimensional array

a = np.array([0, 1, 2, 3, 4, 5])
print(a)
print(type(a))
print(a.shape)  # gives the shape of the array

# range function
b = np.arange(6)  # gives array from 0 to n-1
print(b)

# step
c = np.arange(0, 11, 2)  # start, end, step
print(c)

# zeros
d = np.zeros(10)  # gives array of 10 zeros
print(d)

# Multidimensional zeros
e = np.zeros((3, 4))  # gives 3x4 array of zeros
print(e)

# Full 
f = np.full((10), 5)  # gives array of 10 fives
print(f)

# Multidimensional full 
g = np.full((3, 4), 7)  # gives 3x4 array of sevens
print(g)

# conversion of list to numpy array
list1 = [1, 2, 3, 4, 5]
h = np.array(list1)
print(h)