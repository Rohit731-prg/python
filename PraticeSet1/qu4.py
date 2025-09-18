# Python Program to Find Numbers Divisible by Another Number

def checkDiv(num, div):
    if (num % div == 0):
        return True
    else:
        return False
    
num = int(input("Enter Number : " ))
div = int(input("Enter divisable number : "))
re = checkDiv(num, div)
if (re):
    print("Number is divisible")
else:
    print("Number is not divisable")