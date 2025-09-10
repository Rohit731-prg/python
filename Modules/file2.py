import mod2

loop = True
while loop:
    print("1. Power")
    print("2. Large and Small of three numbers")
    print("3. Swap two numbers")

    ch = int(input("Enter your choice: "))
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if (ch == 1):
        re1 = mod2.power(num1, num2)
        print(f"{num1} raised to the power {num2} is {re1}")
    elif (ch == 2):
        large, small = mod2.larger_smaller(num1, num2)
        print(f"Larger number is {large} and smaller number is {small}")
    elif (ch == 3):
        num1, num2 = mod2.swap(num1, num2)
        print(f"After swapping: First number is {num1} and second number is {num2}")
    else:
        print("Invalid choice");
    is_loop = input("Do you want to continue (y/n): ")
    if (is_loop.lower() != "y"):
        loop = False