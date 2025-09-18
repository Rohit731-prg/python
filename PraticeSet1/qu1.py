# Python Program to Print the Fibonacci sequence

def fibo(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    elif n == 2:
        print(a)
        print(b)
    else:
        print(a, b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

num = int(input("Enter the number of terms: "))
fibo(num);