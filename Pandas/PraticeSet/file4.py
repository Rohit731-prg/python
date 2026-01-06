# replace - to NaN

import pandas as pd

data = pd.read_csv("employees.csv")
data["COMMISSION_PCT"] = data["COMMISSION_PCT"].astype(str).str.strip().replace( '-', 'NaN')
print(data.head(10))