# adding and removeing data with numpy

import numpy as np

arr1 = np.arange(10)
arr2 = arr1[::-1]

combine = np.concatenate((arr1, arr2))
print(combine)
# get total element number from a array
print(combine.shape)

# adding a row/column
original = np.array([[1, 2],
                     [3, 4]])
new_one = np.array([[5, 8]])

# add with row
with_new_row = np.vstack((original, new_one))
print(with_new_row)

# add with column
col = np.array([[7], [8]])
with_new_col = np.hstack((original, col))
print(with_new_col)