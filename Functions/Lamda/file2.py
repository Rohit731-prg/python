gcd = lambda x, y : x if y == 0 else gcd(y, x % y)

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))

result = gcd(num1, num2)
print(f"GCD of {num1} and {num2} is {result}")