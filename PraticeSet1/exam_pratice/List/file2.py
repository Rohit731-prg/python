# check an element in a tuple of tuples

tp = (('a', 'b'), ('c', 'd'), ('e', 'f'))
item = input("Enter an element to check: ")

for i in tp:
    for j in i:
        if j == item:
            print(f"{item} is found in the tuple.")
            exit()

print(f"{item} is not found in the tuple.")