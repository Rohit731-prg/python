# find the employees who earns more then 3000

import pandas as pd

data = pd.read_csv("employees.csv")
print(data[data["SALARY"] > 3000])