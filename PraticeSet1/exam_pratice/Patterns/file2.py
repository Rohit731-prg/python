# 1
# 12
# 123

limit = int(input("Enter the number of rows: "))

for i in range(1, limit + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()