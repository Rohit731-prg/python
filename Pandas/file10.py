import pandas as pd

mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': None, 'b': 2000, 'c': 3000, 'd': 4000}]
df = pd.DataFrame(mydict)

print("Original DataFrame:")
print(df)
print("----------------------------------")

# Fill missing values in column 'a' with its mean
df.fillna({'a': df['a'].mean()}, inplace=True)

print("DataFrame after filling 'a' with its mean:")
print(df)