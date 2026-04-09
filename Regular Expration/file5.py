# check valid password
# 1. length is at least 8,
# 2. contains at least one digit and one uppercase letter,
# 3. contains no spaces,
# 4. it should consist of special character

import re

def validation_check(password: str) -> bool:
    pattern = r"[a-zA-Z0-9]"
    
    if len(password) < 8:
        return False
    if not re.search(pattern, password):
        return False
    if not re.search(r'\d', password):
        return False
    if re.search(r'\s', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

password = input("Enter your password: ")
if validation_check(password):
    print("Valid password")
else:
    print("Invalid password")