# example for filter in python

# li = ["apple", "banana", "avocado", "cherry", "apricot"]
# res = filter(lambda x: x.startswith("a"), li)
# print(list(res))

# li = ["apple", "banana", "avocado", "cherry", "apricot"]
# res = filter(lambda x: x if len(x) > 5 else None, li)
# print(list(res))

# example for map in python

# a = [1, 2, 3, 4]
# res = map(lambda x: x ** 2, a)
# print(list(res))

# li = ["apple", "banana", "avocado", "cherry", "apricot"]
# res = map(lambda x: x[0].upper() + x[1:], li)
# print(list(res))

# example for reduce in python
from functools import reduce

# lst = [1, 2, 3, 4]
# def sum(x, y):
#     return x + y

# res = reduce(sum, lst)
# print(res)

lst = [1, 2, 3, 4]
res = reduce(lambda x, y: x * y, lst)
print(res)