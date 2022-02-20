items = [2, -7, 5, -64, -14]

# ----- Method 1 ----- #
# positive = len([item for item in items if item >= 0])
# negative = len([item for item in items if item <= 0])
# print(positive,negative)

# ----- Method 2 ----- #
# positive = len(list(filter(lambda item:item >= 0,items)))
# negative = len(list(filter(lambda item:item <= 0,items)))
# print(positive,negative)


# ----- Method 3 ----- #
# positive_count = 0
# negative_count = 0

# for i in range(len(items)):
#     if items[i] >= 0:
#         positive_count += 1
#     else:
#         negative_count += 1

# print(positive_count,negative_count)

# ----- Method 4 ----- #

i = 0
positive_count = 0
negative_count = 0

while i < len(items):
    if items[i] >= 0:
        positive_count += 1
    else:
        negative_count += 1
    i += 1

print(positive_count,negative_count)
