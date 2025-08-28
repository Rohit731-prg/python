arr = []

num = int(input("Enter the size of the List: "))
for i in range(num):
    ele = int(input("Enter the Element: "))
    arr.append(ele)
max = min = arr[0]

for i in arr:
    if (i > max):
        max = i

    if (i < min):
        min = i

print(f"Maximum Element: {max}")
print(f"Minimum Element: {min}")