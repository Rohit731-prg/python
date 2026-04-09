list = []
limit = int(input("Enter the number of elements: "))
for i in range(limit):
    element = int(input("Enter element: "))
    list.append(element)

# removed duplicates
remoded_list = []
for i in list:
    if i not in remoded_list:
        remoded_list.append(i)

another_way = set(list)  # using set to remove duplicates
print("List after removing duplicates:", remoded_list)
print("List after removing duplicates:", another_way)

# find 2nd largest number
