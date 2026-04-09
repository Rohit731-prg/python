import re

pattern = "[a-zA-Z0-9]+@(gmail|edu).(com|org|net)"
gmail = input("Enter your email: ")

# if (re.search(pattern, gmail)):
#     print("Valid email")
# else:
#     print("Invalid email")

if (re.match(pattern, gmail)):
    print("Valid email")
else:
    print("Invalid email")