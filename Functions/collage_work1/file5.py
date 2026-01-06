# find GCD of two numbers using recursion

def gcd(a, b, smaller):
    if smaller == 0:
        return 1
    if a % smaller == 0 and b % smaller == 0:
        return smaller
    return gcd(a, b, smaller - 1)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
smaller = min(num1, num2)

print("GCD is:", gcd(num1, num2, smaller))
