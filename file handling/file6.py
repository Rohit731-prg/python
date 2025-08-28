file1 = open("./files/file2.txt", "r")
content = file1.read()
file1.close()

file2 = open("./files/file.txt", "a")
file2.write(content)
print("Successfully written to the file")
file2.close()