# print fibonocci series up to n terms using recursion

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter number of terms: "))
print("Fibonacci series:")
for i in range(1, num + 1):
    print(fibonacci(i), end=' ')