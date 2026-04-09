# count the duplicates in a list of tuples

tp = [('a', 'b'), ('c', 'd'), ('e', 'f'), ('a', 'b')]

duplicates = {}
count = 0

for i in tp:
    for j in tp:
        if i == j:
            count += 1
    if count > 1:
        duplicates[i] = count
    count = 0

print("Duplicates in the list of tuples:")
if duplicates:
    for key, value in duplicates.items():
        if value > 1:
            print(f"{key} appears {value} times.")
else:
    print("No duplicates found.")