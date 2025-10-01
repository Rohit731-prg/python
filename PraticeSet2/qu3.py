# Get File Creation and Modification Date

import os
import datetime # datetime package

file_path = "file/file1.txt"

# creation time
row_time = os.path.getctime(file_path)
creation_time = datetime.datetime.fromtimestamp(row_time)
print("File Creating time : ", creation_time)

# last update time
row_time = os.path.getmtime(file_path)
update_time = datetime.datetime.fromtimestamp(row_time)
print("\nLast Update time : ", update_time)