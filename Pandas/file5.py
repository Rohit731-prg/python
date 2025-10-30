# manupulate data

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
df.loc[1, "city"] = "Joygachi"

print(df)
print("----------------------------------")
# manupulate multiple data

df['marks'] = df['marks'].apply(lambda x: x + 10)
print(df)