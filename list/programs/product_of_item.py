# ----- Method 1 ----- #
# def product_of_items(items):
#     res = 1
#     for item in items:
#         res *= item
#     return res

# items = [1, 3, 5, 6, 3, 5, 6, 1]
# print(product_of_items(list(set(items))))

# ----- Method 2 ----- #

from functools import reduce

items = [1, 3, 5, 6, 3, 5, 6, 1]
print(reduce(lambda item,total:item*total,set(items)))