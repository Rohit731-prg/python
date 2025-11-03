import numpy as np
import matplotlib.pyplot as plb

sales_data = np.array([
    [1, 15000, 18000, 22000, 25000],
    [2, 12000, 14000, 21000, 24000],
    [3, 18000, 20000, 23000, 27000],
    [4, 16000, 19000, 20000, 26000],
    [5, 13000, 15000, 17000, 19000]
])

print("Sales Data shape: ", sales_data.shape)
print("1st 3 resturent data: \n", sales_data[0:3, 1:])
print("Total sales: \n", np.sum(sales_data[:, 1:], axis=0))