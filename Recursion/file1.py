def recursion(num):
    if (num == 1):  # base case
        print(1)
        return
    print(num)
    recursion(num - 1)  # recursive call

num = int(input("Enter Limit : "))
recursion(num)