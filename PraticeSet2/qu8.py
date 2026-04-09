# Write a Python Program to copy the content of one file to another.

import os

source_file = "file/file1.txt"
destination_file = "file/file2.txt"

try:
    if not os.path.exists(source_file) or not os.path.isfile(source_file):
        raise FileNotFoundError(f"The source file '{source_file}' does not exist or is not a file.")
    
    with open(source_file, 'r') as src:
        content = src.read()

    with open(destination_file, 'w') as dst:
        dst.write(content)
except Exception as e:
    print(f"An error occurred: {e}")