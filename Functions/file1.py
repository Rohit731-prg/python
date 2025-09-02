# create a program that provides multiple functionality with iteartion

def take_One_inputs():
    num = int(input("Enter Number : "))
    return num


def check_oddOrEven(num):
    result = "Even" if num % 2 == 0 else "Odd"
    print(f"{num} is an {result} number")

def prime_number(num):
    count = 0
    for i in range(1, num + 1):
        if (num % i == 0):
            count += 1
    
    if (count == 2):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

def armstrong_number(num):
    power = len(str(num))
    sum = 0
    temp = num
    while (temp > 0):
        reminder = temp % 10
        sum += reminder ** power
        temp //= 10
    
    if (sum == num):
        print(f"{num} is an armstrong number")
    else:
        print(f"{num} is not an armstrong number")
    
def neon_number(num):
    squre = num ** 2
    sum_of_digit = 0
    temp = squre
    while (temp > 0):
        reminder = temp % 10
        sum_of_digit += reminder
        temp //= 10

    if (sum_of_digit == num):
        print(f"{num} is a neon number")
    else:
        print(f"{num} is not a neon number")

def palindrom_number(num):
    reverce = 0
    temp = num
    while(temp > 0):
        reminder = temp % 10
        reverce = reverce * 10 + reminder
        temp //= 10
    
    if (reverce == num):
        print(f"{num} is a palindrom number")
    else:
        print(f"{num} is not a palindrom number")

def perfect_number(num):
    temp = num
    sum = 0
    for i in range (1, num):
        if (num % i == 0):
            sum += i
    if (sum == temp):
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")

def automorphic_number(num):
    squre_number = num ** 2
    if (num % 10 == squre_number % 10):
        print(f"{num} is an automorphic number")
    else:
        print(f"{num} is not an automorphic number")

def haesed_number(num):
    sum = 0
    temp = num
    while (temp > 0):
        reminder = temp % 10
        sum += reminder
        temp //= 10
    
    if (num % sum == 0):
        print(f"{num} is a harshad number")
    else:
        print(f"{num} is not a harshad number")


def strong_number(num):
    temp = num
    sum = 0
    while (temp > 0):
        reminder = temp % 10
        f = 1
        for i in range (1, reminder + 1):
            f *= i
        sum += f
        temp //= 10
    if (num == sum):
        print(f"{num} is a strong number")
    else:
        print(f"{num} is not a strong number")

def spy_number(num):
    sum = 0
    product = 1
    temp = num

    while (temp > 0):
        reminder = temp % 10
        sum += reminder
        product *= reminder
        temp //= 10
    
    if (sum == product):
        print(f"{num} is a spy number")
    else:
        print(f"{num} is not a spy number")
    

is_loop = True
while(is_loop):
    print("1. Check number is even or odd")    
    print("2. Check number is Prime or not")    
    print("3. Check number is Armstrong or not")    
    print("4. Check number is Palindrome or not")    
    print("5. Check number is Perfect or not")    
    print("6. Check number is Automorphic or not")    
    print("7. Check number is Harshad or not")    
    print("8. Check number is Strong or not")    
    print("9. Check number is Spy or not")    
    print("10. Check number is Neon or not")
    try:
        print("\n")
        ch = int(input("Enter Your Choice : "))
    except Exception as e:
        print("Invalid Choice : ", e)
        exit()
    num = take_One_inputs()
    if (ch == 1):
        check_oddOrEven(num)
    elif (ch == 2):
        prime_number(num)
    elif (ch == 3):
        armstrong_number(num)
    elif (ch == 4):
        palindrom_number(num)
    elif (ch == 5):
        perfect_number(num)
    elif (ch == 6):
        automorphic_number(num)
    elif (ch == 7):
        haesed_number(num)
    elif (ch == 8):
        strong_number(num)
    elif (ch == 9):
        spy_number(num)
    elif (ch == 10):
        neon_number(num)
    else:
        print("Invalid Choice")
    print("\n-----------------------\n")
    print("Do you want to continue (y/n): ")
    ans = input()
    if (ans.lower() == "y"):
        pass
    else:
        is_loop = False
