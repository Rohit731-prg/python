# Check if a number is divisible by both 3 and 5.

num = int(input("Enter the Number : "))
if ( num % 3 == 0 & num % 5 == 0):
    print("Number is disible")
else:
    print("Number is not disible")

# Check if a given year is a leap year.

year = int(input("Enter Year : "))
if ( year % 4 == 0 & year % 100 ):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")