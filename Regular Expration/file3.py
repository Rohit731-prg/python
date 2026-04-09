import re

try:
    pattern = r"^\+[0-9]{2} [0-9]{10}$"
    number = input("Enter your phone number: ")

    if (re.search(pattern, number)):
        print("Valid phone number")
    else:
        print("Invalid phone number")

except Exception as e:
    print("An error occurred:", e)