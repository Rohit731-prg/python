import pandas as pd

data = {
    "student1": [1, "Rohit", 25, "Delhi"],
    "student2": [2, "Indroit", 25, "Habra"],
    "student3": [3, "Rakesh", 25, "Guma"],
    "student4": [4, "Abinash", 25, "Bira"],
    "student5": [5, "kakhat", 25, "Barasat"],
}

df = pd.DataFrame(data)
# print(df)
df.to_csv("data.csv", index=False)
print(df)
print("--------------x--------------")
print(df.head(1))
print("--------------x--------------")
print(df.tail(1))