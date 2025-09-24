# check weather a string is a palindrom or Not

def palindrom(str):
    newStr = str[::-1]
    if(newStr == str):
        return True
    else:
        return False

str = input("Enter your string : ")
result = palindrom(str)

if result:
    print("String is a palindrom")
else:
    print("String is not a palindrom")