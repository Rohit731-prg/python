# implement the factorial using recursion

def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)

num = int(input("Enter the number: "))
result = fact(num)
print(result)