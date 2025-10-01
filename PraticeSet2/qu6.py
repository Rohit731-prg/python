# Iterate Through Two Lists in Parallel

myList1 = [10, 30, 40, 15, 45, 85]
myList2 = ["Rohit", "Saikat", "Abinash", "Shubham"]

for i, j in zip(myList1, myList2):
    print("First List : ", i, "Second List : ", j)