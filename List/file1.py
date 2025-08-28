arr = []
num = int(input("Enter the size of the List: "))
for i in range(num):
    ele = int(input("Enter the Element: "))
    arr.append(ele)

# in build

arr.sort()
print(arr)

# manual sorting

for i in range (num):
    for j in range (i + 1, num):
        if (arr[i] > arr[j]):
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t


print(arr)