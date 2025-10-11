# Python Program to Check the File Size

import os

print(os.listdir())
file_path = "problem_set1.txt"
if not (os.path.exists(file_path)):
    print("File is not exist")
    exit()
file_size = (os.path.getsize(file_path)) / 1000
print(f"File size of qu.py is {file_size}kb")