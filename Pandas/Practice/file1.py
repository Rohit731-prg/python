import pandas as pd

data = {
    "name": ["Amit", "Riya", "Jhon"],
    "age": [20, 30, 25],
    "marks": [65, 66, 87]
}

df = pd.DataFrame(data)
print(df)

print("First 2 rowa")
print(df.head(2))

print("Column names")
print(list(df.columns))

print("Shape of datafram")
print(df.shape)