# Python Program to Differentiate Between del, remove, and pop on a List

class listFunction:
    def __init__(self, myList):
        self.myList = myList

    def delFun(self):
        index = int(input("Enter the index : "))
        if index > len(self.myList) or index < 0:
            print("Invalid index number.")
            return

        del self.myList[index]
        print("Element deleted..")

    def removeFun(self):
        value = int(input("Enter Element : "))
        if value not in self.myList:
            print("Invalid Element..")
            return
        
        self.myList.remove(value)
        print("Element deleted..")


    def popFun(self):
        self.myList.pop()
        print("Last Element is deleted..")

myList = [10, 30, 15, 75, 80, 65, 45]
print("Old List : ", myList)
myFun = listFunction(myList)

print("1. Delete element with index value")
print("2. Delete element with value")
print("3. Delete element at the last")

ch = int(input("\n\nEnter Choice : "))
if ch == 1:
    myFun.delFun()
elif ch == 2:
    myFun.removeFun()
elif ch  == 3:
    myFun.popFun()
else:
    print("Invalid Choice..!")

print("New List : ", myList)