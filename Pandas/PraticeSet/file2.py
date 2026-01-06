# display each column data type

import pandas as pd

data = pd.read_csv("employees.csv")
print(data.dtypes)