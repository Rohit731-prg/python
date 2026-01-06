#  check the number is armstrong or not

def armstrong(num):
    length = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        reminder = temp % 10
        sum += reminder**length
        temp //= 10
    if sum == num:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

num = int(input("Enter a number: "))
armstrong(num)