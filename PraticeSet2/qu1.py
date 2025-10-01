# Python Program to Get Line Count of a File

import os

if not os.path.exists("file"):
    print("Folder and file does not exist")
    exit()

file_pointer = open("file/file1.txt", "r")
count = 0

for i in file_pointer:
    count += 1

print("Total Line : ", count)
