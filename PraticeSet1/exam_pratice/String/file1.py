str = input("Enter a string: ")

# count vowels
vowels = "aeiouAEIOU"
count = 0
for i in str:
    if i in vowels:
        count += 1
print("Number of vowels in the string:", count)

# reverse a str without using slicing
reversed_str = []
for i in str:
    reversed_str.append(i)
reversed_str.reverse()
reversed_str = ''.join(reversed_str)
print("Reversed string:", reversed_str)

# check if the string is a palindrome
if str == str[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")