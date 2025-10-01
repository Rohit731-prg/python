# Check the File Size

import os

file_path = "file/file1.txt"
total_size = os.path.getsize(file_path)
print("Total size of file is ", total_size, "in bytes")