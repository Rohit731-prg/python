import matplotlib.pyplot as plt
import numpy as np

data1 = np.array([15, 45, 75, 48, 55])
data2 = np.array([45, 75, 11, 56, 44])

names = ["rohit", "shuvam", "souvik", "rick", "abinash"]

plt.xlabel("Names of Students")
plt.ylabel("Marks")

plt.title("graph of student marks")

plt.plot(names, data1, color="red", label="English", marker="o")
plt.plot(names, data2, color="blue", label="Math", marker="o")

plt.legend()
plt.show()