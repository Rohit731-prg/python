# Capitalize the First Character of a String

myStr = input("Enter your string : ")
first_char = myStr[0].upper()
new_str = myStr.replace(myStr[0], first_char)

print("New String : ", new_str)