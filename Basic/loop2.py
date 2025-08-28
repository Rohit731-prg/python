# Find the factorial of a given number.

sum = 0
num = int(input("Enter the Number : "))
while (num > 0):
    r = num % 10;
    f = 1
    for i in range(1, r + 1):
        f *= i
    sum += f
    num /= 10

print(f"{num} factorial is {sum}")