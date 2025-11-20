# Sorting

import pandas as pd
import numpy as np

data = pd.read_csv('demo3.csv')
df = pd.DataFrame(data)
arr = np.array(df)

sorted_indices = np.argsort(arr[:, 8].astype(float))
sorted_array = arr[sorted_indices]

sorted_df = pd.DataFrame(sorted_array, columns=df.columns)
print(sorted_df)