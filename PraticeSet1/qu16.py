# Check if Two Strings are Anagram

def check(str1, str2):
    if (len(str1) != len(str2)):
        return False
    
    if (sorted(str1) == sorted(str2)):
        return True
    else:
        return False

str1 = input("Enter 1st String : ")
str2 = input("Enter 2nd String : ")

result = check(str1, str2)
if result:
    print("2 String are Anagram")
else:
    print("2 String are not Anagram")