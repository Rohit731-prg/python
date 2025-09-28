import os

sourse_file = "./files/noice2.txt"
destination_file = "./files/noice.txt"

try:
    os.rename(sourse_file, destination_file)
    print("File renamed successfully")
except:
    print("Failed to rename the file")