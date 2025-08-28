text = open("./files/file3.txt", "a")
num = text.write("\nthis is a sunny day and we are enjoing our day in office....what a joke!")
if (num):
    print("Successfully written to the file")
else:
    print("Failed to write to the file")
text.close()