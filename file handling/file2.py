file = open("./files/file2.txt", "a")
file.write("\nHello World")
file.close

file = open("./files/file2.txt", "r")
print(file.read())
file.close