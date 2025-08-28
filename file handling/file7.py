search = input("Enter the word you want to search: ")
file = open("./files/file3.txt", "r")

count = 0
for i in file:
    for i in i.split():
        if (i == search):
            count += 1

if (count == 0):
    print(f"{search} is not present in the file")
else:
    print(f"{search} is present {count} times in the file")