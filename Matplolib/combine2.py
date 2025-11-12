# Basic Calculations

import pandas as pd
import numpy as np

data = pd.read_csv('demo2.csv')
df = pd.DataFrame(data)
arr = np.array(df)

units_sold = arr[:, 5]
unit_price = arr[:, 6]
discount = arr[:, 7]

total_sales = units_sold * unit_price * (1 - discount)
df["Total_sales"] = total_sales

print(df)

df.to_csv("demo3.csv", index=False)