fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)

n = int(input("Enter number: "))

for i in range(n):
    print(fib(i), end=" ")