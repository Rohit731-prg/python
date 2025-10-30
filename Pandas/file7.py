# clean data

import pandas as pd

data = {
    "name": ["Rohit", "Saptorshi", "Souvik", "Rupom", "Choyan"],
    "marks": [56, 76, 78, 45, 86],
    "city": ["Delhi", "Habra", "Guma", "Bira", "Barasat"],
    "country": ["India", "India", None, "India", "India"]
}

df = pd.DataFrame(data)
print(df)
print("----------------------------------")

print(df.isnull())
print(df.isnull().sum())