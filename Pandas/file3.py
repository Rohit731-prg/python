# shape and size and Columns of dataframe

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
print("Shape of DataFrame:", df.shape)
print("Size of DataFrame:", df.size)
print("Columns of DataFrame:", df.columns)