def power(num1, num2):
    return num1 ** num2

def larger_smaller(num1, num2):
    if num1 > num2:
        large = num1
        small = num2
    else:
        large = num2
        small = num1
    return large, small


def swap(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return num1, num2