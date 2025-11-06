# scatter plot with different marker styles

import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]

x2 = [1, 2, 3, 4, 5]
y2 = [1, 4, 6, 8, 10]

plt.title("Scatter Plot with Different Marker Styles")
plt.scatter(x1, y1, marker='o', color='blue', label='Dataset 1')
plt.scatter(x2, y2, marker='s', color='red', label='Dataset 2')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()
plt.show()