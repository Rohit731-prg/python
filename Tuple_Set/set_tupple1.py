# Write a program to create a tuple of tuple and check the elements in it.

tp = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
element = int(input("Enter an element to check: "))

for i in tp:
    if element in i:
        print(f"Element {element} found in tuple {i}")
        exit();

print(f"Element {element} not found in any tuple")