import os

if (os.path.exists("./files/file3.txt")):
    try:
        os.remove("./files/file3.txt")
        print("File deleted successfully")
    except:
        print("Failed to delete the file")
else:
    print("File not found")