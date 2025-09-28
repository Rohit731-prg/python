# copy charecters and number in different files from root file

import os

if not (os.path.exists("folder")):
    os.mkdir("folder")
    myStr = "af12w4b7x21c3y6d9z5e2m8"
    file_pointer = open("./folder/root.txt", "x")
    file_pointer.write(myStr);
else:
    print("Folder and files are already exist")
    exit()


numberF = open("./folder/numberFile.txt", "x");
charF = open("./folder/charFile.txt", "x");
numberF.close()
charF.close()
numberF = open("./folder/numberFile.txt", "a");
charF = open("./folder/charFile.txt", "a");


file_pointer.close()
file_pointer = open("./folder/root.txt", "r")
for i in file_pointer:
    for j in i:
        if j.isdecimal():
            numberF.write(j)
        else:
            charF.write(j)


print("Task complite ! there should be your folder and files exist")