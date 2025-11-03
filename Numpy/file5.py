# reshape and flatten and transpose

import numpy as np

org = np.arange(15)
print("Original Array: ", org)

reshapeOrg = org.reshape((5, 3))
print("reshape Array: ", reshapeOrg)

fla = reshapeOrg.flatten()
print("flatten Array: ", fla)

transpose = reshapeOrg.T
print("Transpose Array: ", transpose)
print(fla[2:3])