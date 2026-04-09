import pandas as pd

data = {
 "Product": ["Pen", "Pencil", "Eraser"],
 "Price": [10, 5, 3],
 "Stock": [100, 150, 200]
}

df = pd.DataFrame(data)
# print("Only Price Column")
# print(df["Price"])

print(df.loc[0])
res = df.loc[0: 3][["Stock", "Price"]]
print(res)