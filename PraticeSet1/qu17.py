# Count the Number of Digits Present In a Number

myStr = int(input("Enter Number : "))
count = 0

while(myStr > 0):
    count += 1
    myStr = myStr // 10

print("Total Digits : ", count)
