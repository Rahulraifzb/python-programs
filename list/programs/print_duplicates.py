items = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

# ----- Method 1 ----- #
print(list(set([item for item in items if items.count(item) > 1])))

# ----- Method 2 ----- #

duplicates = []
for i in range(len(items)):
    if items.count(items[i]) > 1 and items[i] not in duplicates:
        duplicates.append(items[i])
print(duplicates)
