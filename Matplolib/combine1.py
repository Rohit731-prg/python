# Read & Inspect Data

import pandas as pd
import numpy as np

df = pd.read_csv('demo2.csv')
data = pd.DataFrame(df)
arr = np.array(data)

print(arr[0:5, :])