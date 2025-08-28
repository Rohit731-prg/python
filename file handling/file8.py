file = open("./files/file3.txt", "r")
current_location = file.tell()
print(current_location)
file.close()