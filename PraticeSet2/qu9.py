# check given string is palindrome or not

def is_palindrom(str: str) -> bool:
    reverceStr = str[::-1]
    return str == reverceStr

str = input("Enter a string: ")
if is_palindrom(str):
    print(f"{str} is a palindrome.")
else:
    print(f"{str} is not a palindrome.")