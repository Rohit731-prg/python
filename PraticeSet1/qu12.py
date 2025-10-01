# Remove duplicate elements from a list

def removeDuplicate(myList):
    result = []
    for i in myList:
        if (i not in result):
            result.append(i)

    print("Original List : ", myList)
    print("Filtered List : ", result)

myList = [10, 20, 30, 60, 40, 10, 15, 20]
removeDuplicate(myList)
