# Write a python program to remove duplicates from a list of tuples.

tp = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (7, 8)]

newSet = set(tp)
newList = list(newSet)
print("List after removing duplicates:", newList)