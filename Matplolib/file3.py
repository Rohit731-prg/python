# bar chat in matplotlib

import matplotlib.pyplot as plt

category = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 30, 40, 50]

plt.bar(category, values)
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.grid()

plt.show()