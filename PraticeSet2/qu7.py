# - Write a Python Program to count the occurrence of each character in your name. 

def count_chars(name: str) -> dict:
    char_dict = {}
    name = name.replace(" ", "")  # Remove spaces from the name
    for char in name:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

name = input("Enter your name: ")
char_count = count_chars(name)
print("Character occurrence in your name:")
print(char_count)