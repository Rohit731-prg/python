# convert decimal to binary using recursion

def convert(num, result):
    if num == 0:
        return
    convert(num // 2, result)
    result.append(num % 2)

num = int(input("Enter the number: "))
result = []
convert(num, result)
print(result)