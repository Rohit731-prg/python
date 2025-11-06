# grids in matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 3, 5, 7, 1])

plt.grid()
plt.plot(x, y1, marker='.', linestyle='-', markerfacecolor='c', markersize=10)

plt.show()