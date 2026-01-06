# convert hier-date in proper dateformat

import pandas as pd

data = pd.read_csv("employees.csv")
data["HIRE_DATE"] = pd.to_datetime(data["HIRE_DATE"], format="%d-%b-%y", errors='coerce')
print(data.dtypes)
