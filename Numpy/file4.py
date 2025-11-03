# random operations with numpy

import numpy as np

random = np.random.rand(2) * 100
print(random)

# random matrix
random1 = np.random.random((3, 3))
print(random1)

# tenser
tensor = np.array([[[10, 20], [20, 30]],
                   [[30, True], [40, 50]],
                   [[50, 60], [60, 70]]])

print(tensor)