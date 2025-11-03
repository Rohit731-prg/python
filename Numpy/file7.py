# masking in numpy

import numpy as np

arr = np.arange(0, 20, 2)
print(arr)
mask = arr > 5
print(mask)
print(arr[mask])
print(mask.reshape(2, 5))

# where in numpy
print("____________________")
indesx = [0, 3, 6, 9]
print(arr[indesx])
print("gretter then 10", np.where(arr > 10))