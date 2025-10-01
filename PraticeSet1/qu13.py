# count a charecter occourence in a string

def countChar(myStr, char):
    count = 0

    for i in myStr:
        if (i.lower() == char.lower()):
            count += 1

    return count

myStr = input("Enter your String : ")
char = input("Enter charecter : ")

result = countChar(myStr, char)
print(f"{char} is appear {result} times")