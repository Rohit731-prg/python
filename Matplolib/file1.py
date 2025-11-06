import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 3, 5, 7, 1])
y2 = np.array([2, 9, 2, 15, 4])

plt.title("Customized Markers Example")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

plt.plot(x, y1, marker='.', linestyle='-', markerfacecolor='c', markersize=10)
plt.plot(x, y2, marker='o', linestyle='-', markerfacecolor='r', markersize=10)
plt.show()