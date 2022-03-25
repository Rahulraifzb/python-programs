from os import remove


items1 = [1, 2, 3, 4, 5]  
items2 = [4, 5, 6, 7, 8]

# ----- Method 1 ----- #
print(list(set(items1) & set(items2)))

# ----- Unique finder in list ----- #
# unique = []
# for item in items1[:]:
#     if item not in items2:
#         unique.append(item)
# print(unique)

# ----- Method 2 ----- #
# for item in items1[:]:
#     if item in items2:
#         items1.remove(item)
#         items2.remove(item)
# print(items1,items2)


# ----- Method 3 ----- #
def remove_common(a,b):
    a,b = [item for item in items1 if item not in b],[item for item in items2 if item not in a]
    return a,b

print(remove_common(items1,items2))

