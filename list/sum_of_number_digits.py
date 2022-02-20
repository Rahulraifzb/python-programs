from functools import reduce


items = [12, 67, 98, 34]


# ----- Method 2 ----- #
# new_items = []
# for item in items:
#     total = 0
#     for digit in str(item):
#         total += int(digit)
#     new_items.append(total)

# print(new_items)

# ----- Method 3 ----- #
# new_lists = list(map(lambda item:sum(int(digit) for digit in str(item)),items))

# print(new_lists)

# ----- Method 4 ----- #

new_lists = [reduce(lambda x,y: int(x) + int(y),list(str(item)))  for item in items]

print(new_lists)