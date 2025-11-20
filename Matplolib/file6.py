# histogram in matplotlib
import numpy as np
import matplotlib.pyplot as plt

scores = np.random.normal(loc=80, scale=10, size=100)
print(scores)
plt.hist(scores)

plt.show()