file_read = open("./files/file.txt", "r")
file_read_create = open("./files/file2.txt", "x")
print(file_read.read())

file_read_create.write("Hello World")
file_read_create.close()