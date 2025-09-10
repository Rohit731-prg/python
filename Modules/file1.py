import mod1

loop = True
while loop:
    print("1. Check Palindrome")
    print("2. Check Prime")
    print("3. Calculate Factorial")
    ch = int(input("Enter your choice: "))
    num = int(input("Enter a number: "))
    if (ch == 1):
        mod1.palindrom(num)
    elif (ch == 2):
        mod1.prime(num)
    elif (ch == 3):
        mod1.factorial(num)
    else:
        print("Invalid choice");

    is_loop = input("Do you want to continue (y/n): ")
    if (is_loop.lower() != "y"):
        loop = False