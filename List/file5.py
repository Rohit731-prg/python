arr = []

num = int(input("Enter the size of the List: "))
for i in range(num):
    ele = int(input("Enter the Element: "))
    arr.append(ele)

div = int(input("Enter the Divisor: "))

if div == 0:
    print("Divisor cannot be 0")
    exit()
if div > num:
    print("Divisor cannot be greater than List size")
    exit()

split = []
chunk_size = num // div
remainder = num % div
start = 0

for i in range(div):
    end = start + chunk_size + (1 if i < remainder else 0)
    split.append(arr[start:end])
    start = end

print("\nSplit List:")
for i in split:
    print(i)