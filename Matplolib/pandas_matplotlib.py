import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('demo.csv')

type1_count = df['Type1'].value_counts()

plt.barh(type1_count.index.tolist(), type1_count.values.tolist())
plt.show()