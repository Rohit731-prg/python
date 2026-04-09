# Write a Python Program to extract phone numbers and valid email id from raw text.

import re

patern = r"\d{10}|[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[(com|in|org|net)]{2,4}"
text = "My name is John Doe. You can contact me at 1234567890 or email me at john.doe@example.com"

matches = re.findall(patern, text)
print("Extracted phone numbers and email ids:")
for i in matches:
    print(i)