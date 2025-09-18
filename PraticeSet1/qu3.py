# Python Program to Display Powers of 2 Using Anonymous Function

num = int(input("Enter Your Limit : "))
myList = list(map(lambda x: 2**x, range(num)))

print(myList)