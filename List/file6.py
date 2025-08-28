arr = []
num = int(input("Enter the size of the List: "))
for i in range(num):
    ele = int(input("Enter the Element: "))
    arr.append(ele)


odds = []
evens = []

for i in arr:
    if (i % 2 == 0):
        evens.append(i)
    else:
        odds.append(i)

print(f"Odd Elements: {odds}")
print(f"Even Elements: {evens}")