import numpy as np

sales_data = np.array([
    [1, 15000, 18000, 22000, 25000],
    [2, 12000, 14000, 21000, 24000],
    [3, 18000, 20000, 23000, 27000],
    [4, 16000, 19000, 20000, 26000],
    [5, 13000, 15000, 17000, 19000]
])

print("Sales Data shape: ", sales_data.shape)
print("1st resturent data: \n", sales_data[0, 1:])
print("1st 3 resturent data: \n", sales_data[0:3, 1:])
print("Total sales: \n", np.sum(sales_data[:, 1:], axis=0))
print("Minimun sales per resturent: ", np.min(sales_data[:, 1:], axis=1))
print("Maximum sales per year: ", np.max(sales_data[:, 1:], axis=0))
print("Avarage sales of each resturent: ", np.average(sales_data[:, 1:], axis=1))