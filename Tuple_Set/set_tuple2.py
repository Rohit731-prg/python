# Write a Python program to count the duplicates in a list of tuples.

from collections import Counter

tp = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (7, 8)]
# with the help of counter package

count = Counter(tp)
print("Using Counter package:")
for key, value in count.items():
    if value > 1:
        print(f"Tuple {key} has {value} duplicates")

# without using any package
duplicates = {}
count = 0
for i in tp:
    for j in tp:
        if i == j:
            count += 1
    if count > 1:
        duplicates[i] = count
    count = 0

print("\nWithout using any package:")
for key, value in duplicates.items():
    print(f"Tuple {key} has {value} duplicates")