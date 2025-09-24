# impliment sum of natural number using reduce function

def sum_Natual(num):
    if num == 1:
        return 1
    return num + sum_Natual(num-1)

num = int(input("Enter the number: "))
result = sum_Natual(num)
print(result)