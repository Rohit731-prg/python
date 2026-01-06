# display first 5 rows in dataset

import pandas as pd

data = pd.read_csv("employees.csv")
print(data.head(5))