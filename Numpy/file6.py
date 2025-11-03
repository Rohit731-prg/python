# indexing and slicing on 2d array

import numpy as np

mat = np.ones((2, 3))
print(mat)
print("Specific element: ", mat[1, 2])
print("Whole row", mat[1])
print("Whole Column", mat[:, 1])

# sorting array with numpy
unsort = np.array([[[12, 23], [23, 45]],
                   [[85, 75], [84, 96]]])
print(f"Unsorted array: {unsort}")
sorted = np.sort(unsort)
print("Sorted array: ", sorted)
print("x axis sorted", np.sort(sorted, axis=1))

# filtering with arrays in numpy
arr = np.arange(15)
print(arr[arr % 2 == 0])