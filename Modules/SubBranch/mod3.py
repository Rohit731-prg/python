def muFun(myList):
    large = myList[0]
    small = myList[0]

    for i in myList:
        if i > large:
            large = i
        elif i < small:
            small = i
    return (large, small)