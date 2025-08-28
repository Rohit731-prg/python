arr = []

num = int(input("Enter the size of the List: "))
for i in range(num):
    ele = int(input("Enter the Element: "))
    arr.append(ele)

search = int(input("Enter the Element to be Searched: "))

for i in arr:
    if (i == search):
        print(f"Element Found")
        exit()

print("Element Not Found")