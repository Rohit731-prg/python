# Randomly Select an Element From the List

import random

myList = [10, 20, 40, 45, 25, 95]
list_size = len(myList)
randomEle = random.randint(1, list_size) # return int datetype random number
print(myList[randomEle])