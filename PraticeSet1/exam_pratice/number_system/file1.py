# convert decimal to binary
num = int(input("Enter a decimal number: "))
binary = []

while num > 0:
    reminder = num % 2
    binary.append(reminder)
    num = num // 2

binary.reverse()
result = ''.join(str(ch) for ch in binary)
print("Binary representation:", result)