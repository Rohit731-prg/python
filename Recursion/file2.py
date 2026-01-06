def printNum(start, end):
    if start > end:
        return
    print(start)
    printNum(start + 1, end)

end = int(input("Enter Limit : "))
printNum(1, end)