# Filtering

import pandas as pd
import numpy as np

data = pd.read_csv('demo2.csv')
df = pd.DataFrame(data)
arr = np.array(df)

fileter_data = (arr[:, 4] == "Electronics") & (arr[:, 3] == "John")
final_data = df[fileter_data]

print(final_data)