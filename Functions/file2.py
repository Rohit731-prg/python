# create a program that provides multiple functionality with iteartion with List and try catch
class myFun:
    def max_min_element(arr):
        max = min = arr[0]
        for i in arr:
            if (i > max):
                max = i

            if (i < min):
                min = i
        print(f"Maximum Element: {max}")
        print(f"Minimum Element: {min}")

    def reverce_linkList(arr):
        print(arr[::-1])

    def palindrome(arr):
        newArr = arr[::-1]
        if (arr == newArr):
            print("List is Palindrome")
        else:
            print("List is not Palindrome")

    def remove_duplicate(arr):
        arr = list(set(arr))
        print(arr)

    def second_largest_smallest(arr):
        arr.sort()
        print(f"Second Largest Element: {arr[-2]}")
        print(f"Second Smallest Element: {arr[1]}")

is_loop = True
while (is_loop):
    arr = []
    print("Lets Create a List")
    limit = int(input("Enter the size of the List: "))
    for i in range(limit):
        ele = int(input("Enter the Element: "))
        arr.append(ele)
    print("\n\n")
    print("1. Maximum and Minimum Element")
    print("2. Reverse a List")
    print("3. Check if a List is Palindrome or not")
    print("4. Remove Duplicate Elements")
    print("5. Second Largest Element and Second Smallest Element")
    print("\n")
    try:
        ch = int(input("Enter Your Choice : "))
    except Exception as e:
        print("Invalid Choice : ", e)
        exit()

    if (ch == 1):
        myFun.max_min_element(arr)
    elif (ch == 2):
        myFun.reverce_linkList(arr)
    elif (ch == 3):
        myFun.palindrome(arr)
    elif (ch == 4):
        myFun.remove_duplicate(arr)
    elif (ch == 5):
        myFun.second_largest_smallest(arr)
    else:
        print("Invalid Choice")
    
    check = input("Do you want to continue (y/n) : ")
    if (check.lower() == 'y'):
        is_loop = True
    else:
        is_loop = False