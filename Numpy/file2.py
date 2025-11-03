# operations on numpy arrays

import numpy as np

# difference between list and numpy array
list1 = [10, 15, 20]
arr1 = np.array([10, 15, 20])
print(list1 * 2)
print(arr1 * 2)

# basic opertions

ar1 = np.array([10, 20, 30])
ar2 = np.array([5, 25, 35])

print("Addtion: ", ar1 + ar2)
print("Subtraction: ", ar1 - ar2)
print("Multiplication: ", ar1 * ar2)
print("Divition: ", ar1 / ar2)
print("Mod: ", ar1 % ar2)