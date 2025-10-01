# Find All File with .txt Extension Present Inside a Directory

import os

folder_path = "."  # current directory
all_files = os.listdir(folder_path)

for file in all_files:
    if os.path.isfile(os.path.join(folder_path, file)):  # only files
        name, ext = os.path.splitext(file)  # split name and extension
        print(f"{file} --> Extension: {ext}")
