# delete data from a data farme

import pandas as pd

data = {
    "name": ["Rohit", "Saptorshi", "Souvik", "Rupom", "Choyan"],
    "marks": [56, 76, 78, 45, 86],
    "city": ["Delhi", "Habra", "Guma", "Bira", "Barasat"],
    "country": ["India", "India", "India", "India", "India"]
}

df = pd.DataFrame(data)
print(df)
print("----------------------------------")

# delete column
df.drop(columns= ["country"], inplace=True)
print(df)
print("----------------------------------")
# delete row
df.drop(index=[2], inplace=True)
print(df)