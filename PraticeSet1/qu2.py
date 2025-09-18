# Python Program to Find Armstrong Number in an Interval

def armstrong(start, end):
    for i in range(start, end + 1):
        temp = i
        sum = 0
        while (temp > 0):
            reminder = temp % 10
            reminder = reminder ** 3
            sum += reminder
            temp //= 10 
        
        if (sum == i):
            print(f"{i} is a armstrong number")
        else:
            print(f"{i} is not a armstrong number")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
armstrong(start, end)