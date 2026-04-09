# binary to decimal in python

num = input("Enter a binary number: ")
decimal = 0
length = len(num) - 1
for i in num:
    decimal = decimal + (int(i) * (2 ** length))
    length = length - 1

print("Decimal representation:", decimal)