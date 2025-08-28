text = input("Enter the text: ")

file = open("./files/file3.txt", "x")
file.write(text)
file.close