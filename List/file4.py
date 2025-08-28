arr = []
num = int(input("Enter the number of elements: "))
for i in range(num):
    ele = int(input("Enter the Element: "))
    arr.append(ele)

for i in range(num):
    for j in range(i + 1, num):
        if (arr[i] == arr[j]):
            print(f"Duplicate Element: {arr[i]}")
            exit()

print("No Duplicates")