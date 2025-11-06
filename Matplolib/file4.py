# pie chart with percentage labels

import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 35, 20, 20]

plt.title("Pie Chart with Percentage Labels")
plt.pie(values, labels=categories, autopct='%1.1f', shadow=True, explode=(0.1, 0, 0, 0))
plt.show()