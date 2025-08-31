import numpy as np

# universal functions (ufuncs) are functions that operate element-wise on ndarrays

arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

# Example of a ufunc: np.sqrt
sqrt_arr = np.sqrt(arr)
print("Square root of each element:", sqrt_arr)

np2 = np.array([-3, -2, -1, 0, 1, 2, 3])
# absolute value
abs_arr = np.abs(np2)
print("Absolute values:", abs_arr)

# exponential
exp_arr = np.exp(arr)
print("Exponential of each element:", exp_arr)

# min and max
min_val = np.min(arr)
max_val = np.max(arr)
print("Min value:", min_val)
print("Max value:", max_val)

# sign positive, negative, or zero
sign_arr = np.sign(np2)
print("Sign of each element:", sign_arr)    

# trig sin cos log
sin_arr = np.sin(arr)
cos_arr = np.cos(arr)
log_arr = np.log(arr)
print("Natural logarithm of each element:", log_arr)
print("Sine of each element:", sin_arr)
print("Cosine of each element:", cos_arr)

# and much more...

