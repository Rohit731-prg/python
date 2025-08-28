file = open("./files/file2.txt", "r")
line = 0
word = 0
char = 0

for i in file:
    line += 1
    word += len(i.split())
    char += len(i)

print("Line: ", line)
print("Word: ", word)
print("Char: ", char)