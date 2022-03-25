items =  [15, 6, 7, 10, 12, 20, 10, 28, 10,13,19]


# ----- Method 1 ----- #
# print([item for item in items if item % 2 == 1])

# ----- Method 2 ----- #
# print(list(filter(lambda item: item % 2 == 1,items)))

# ----- Method 3 ----- #
# odds = []
# for i in range(len(items)):
#     if items[i] % 2 != 0:
#         odds.append(items[i])
# print(odds)

# ----- Method 4 ----- #
odds = []
i = 0
while i < len(items):
    if items[i] % 2 != 0:
        odds.append(items[i])
    i += 1
print(odds)
