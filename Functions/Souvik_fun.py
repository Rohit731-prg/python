# create a program that provides multiple functionality with iteartion


# User input for value check :

def take_user_input():
    num = int(input("Enter Your value : "))
    return(num)


# Even or Odd number check : 

def check_even_odd(num):
    if(num % 2 == 0):
        print(f"{num} is Even Number")
    else:
        print(f"{num} is Odd Number")

# Prime Number Check : 

def prime_check(num):
    count = 0
    for i in range(1 , num+1):
        if(num%i == 0):
            count += 1

    if(count == 2):
        print(f"{num} is Prime number")
    else:
        print(f"{num} is not Prime number")


# Armstrong Number Check : 

def armstrong(num):
    s = 0
    n = num
    while(num > 0):
        r = num % 10
        s = s + (r**3)
        num = num // 10
 
    if(n == s ):
        print(f"{n} is Armstrong ")
    else:
        print(f"{n} is not Armstrong")


# Neon Number Check...

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



# Palindrome Number Check :

def palindrome(num):
    reverse = 0
    n = num
    while(num > 0):
        reminder = num % 10
        reverse = reverse * 10 + reminder
        num = num // 10

    if(reverse == n):
        print(f"{n} is Palindrome ")
    else:
        print(f"{n} is not Palindrome")


# krishnamurty Number Check :

def krishnamurty(num):
    s = 0
    n = num 
    while(num > 0):
        f = 1
        reminder = num % 10
        for i in range(1, reminder + 1):
            f = f*i
        s += f
        num = num // 10
    
    if(n == s):
        print(f"{n} is krishnamurty")
    else:
        print(f"{n} is not krishnamurty")


# Perfect Number Check...


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


# Harshed Number Check ...


def harshed_number(num):
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

# Strong Number Check ...


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


# Spy number Check ....


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
    print("4. Check number is Neon or not")   
    print("5. Check number is Palindrome or not")
    print("6. Check number is Krishnamurty or not")    
    print("7. Check number is Perfect or not")    
    print("8. Check number is Automorphic or not")    
    print("9. Check number is Harshad or not")    
    print("10. Check number is Strong or not")    
    print("11. Check number is Spy or not")    


    try:
        print("\n")
        ch = int(input("Enter Your Choice : "))
    except Exception as e:
        print("Invalid Choice : ", e)
        exit()

    num = take_user_input()
    if(ch == 1):
        check_even_odd(num)
    elif(ch == 2):
        prime_check(num)
    elif(ch == 3):
        armstrong(num)
    elif(ch == 4):
        neon_number(num)
    elif(ch == 5):
        palindrome(num)
    elif(ch == 6):
        krishnamurty(num)
    elif(ch == 7):
        perfect_number(num)
    elif (ch == 8):
        automorphic_number(num)
    elif (ch == 9):
        harshed_number(num)
    elif (ch == 10):
        strong_number(num)
    elif (ch == 11):
        spy_number(num)

    else:
        print("Invalid Choice")
    print("\n-----------------------\n")
    print("Do you want to continue (y/n): ")
    ans = input()
    if (ans.lower() == "y"):
        pass
    else:
        is_loop = False

    