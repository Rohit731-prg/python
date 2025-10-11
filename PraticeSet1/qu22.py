# Return Multiple Values From a Function

def myFunction(num1, num2):
    sum = num1 + num2
    sub = num2 - num1

    return sum, sub

result1, result2 = myFunction(60, 44)
print("Sun : ", result1)
print("Sub : ", result2)