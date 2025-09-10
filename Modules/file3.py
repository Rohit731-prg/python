import sys
import os

# Build the correct path to SubBranch (case-sensitive and confirmed)
subBranch_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'SubBranch'))
# print("SubBranch Path:", subBranch_path)   # Debugging

sys.path.append(subBranch_path)

import mod3

limit = 5
myList = []
for i in range(limit):
    element = int(input("Enter the element: "))
    myList.append(element)

large, small = mod3.muFun(myList)
print("The largest element is:", large)
print("The smallest element is:", small)
