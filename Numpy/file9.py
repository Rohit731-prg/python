# delete values with numpy

import numpy as np

arr = np.arange(10)
deleted = np.delete(arr, 2)
print(deleted)

print("_______________")
# dots in numpy

ar1 = np.array([10, 20, 30])
ar2 = np.array([5, 25, 35])

print("Dots product: ", np.dot(ar1, ar2))