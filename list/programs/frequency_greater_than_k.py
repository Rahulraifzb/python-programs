# ----- Method 1 ----- #
# items = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# k = 2
# res = []
# for item in items:
#     if items.count(item) > 2 and item not in res:
#         res.append(item)

# print(res)

# ----- Method 2 ----- #
items = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 2
res = list({item for item in items if items.count(item) > k})

print(res)

