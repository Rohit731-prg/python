def palindrom(num):
    sum = 0
    temp = num
    while (num > 0):
        reminder = num % 10
        sum = (sum * 10) + reminder
        num = num // 10
    if (temp == sum):
        print(f"{temp} is a palindrome")
    else:
        print(f"{temp} is not a palindrome")

def prime(num):
    count = 0
    if (num == 1 or num == 0):
        print(f"{num} is not a prime number")
    else:
        for i in range(1, num + 1):
            if (num % i == 0):
                count += 1
        if (count == 2):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(f"The factorial of {num} is {fact}")