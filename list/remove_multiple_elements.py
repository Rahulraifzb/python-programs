# items = [12, 15, 3, 10]


# ----- Removing even number from list ----- #
# for i in range(len(items) - 1):
#     if items[i] % 2 == 0:
#         items.remove(items[i])

# print(items)


# ----- Removing odd number from list ----- #
# for i in range(len(items)-1):
#     if items[i] % 2 != 0:
#         items.remove(items[i])
# print(items)


# ----- Removing element from start to end index ----- #
# del items[1:2]
# print(items)


# items = [11, 5, 17, 18, 23, 50]
# unwanted_num = {11,5}

# print([item for item in items if item not in unwanted_num])

# ----- Method 2 ----- #

# items = [11, 5, 17, 18, 23, 50]
# unwanted_num = [0, 3, 4]
# for item in sorted(unwanted_num,reverse=True):
#     del items[item]
# print(items)

