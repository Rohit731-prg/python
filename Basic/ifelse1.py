# Check if a number is positive, negative, or zero.

num = int(input("Enter Number : "))
if (num == 0):
    print("0 is not allow")
elif (num > 0):
    print(f"{num} is a possitive number")
else:
    print(f"{num} is  negative number")