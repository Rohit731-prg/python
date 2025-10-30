# insert column in data form

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
# df['sec'] = df['marks'].apply(lambda x: "A" if x > 70 else "B")
# print(df)

# using insert method

df.insert(2, "sec", df['marks'].apply(lambda x: "A" if x > 70 else "B"))
print(df)