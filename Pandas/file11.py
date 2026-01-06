import pandas as pd

data = pd.read_csv("employees.csv")
total_len = len(data)
salaries = data['SALARY']

ava = sum(salaries) / total_len
print("Avarage salaries : ", ava)