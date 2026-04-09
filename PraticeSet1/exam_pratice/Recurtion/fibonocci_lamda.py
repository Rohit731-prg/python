# fibonocci series using recursion

fib = lambda n: 0 if n == 1 else 1 if n == 2 else fib(n - 1) + fib(n - 2)

num = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range(1, num + 1):
    print(fib(i), end=' ')