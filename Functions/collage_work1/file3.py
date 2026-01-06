# Function to check if a number is perfect or not

def perfect(num):
    sum = 0
    for i in range(1, num - 1):
        if num % i == 0:
            sum += i

    if sum == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")


num = int(input("Enter a number: "))
perfect(num)