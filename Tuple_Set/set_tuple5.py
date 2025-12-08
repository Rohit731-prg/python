# create two sets with some common elememts and perform union and intersection and difference operations.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

total_list = list(set1) + list(set2)
newLS1 = list(set1)
newLS2 = list(set2)

union = []
intersection = []
difference = []

for i in total_list:
    if i in newLS1 and i in newLS2:
        if i not in intersection:
            intersection.append(i)
    elif i in newLS1 or i in newLS2:
        if i not in difference:
            difference.append(i)

union = intersection + difference

print("Union of set1 and set2 is:", set(union))
print("Intersection of set1 and set2 is:", set(intersection))
print("Symmetric difference of set1 and set2 is:", set(difference))

# with the help of inbuilt functions
print("\nUsing inbuilt functions:")
print("Union of set1 and set2 is:", set1.union(set2))
print("Intersection of set1 and set2 is:", set1.intersection(set2))
print("Symmetric difference of set1 and set2 is:", set1.symmetric_difference(set2))