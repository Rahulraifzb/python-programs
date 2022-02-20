items = [12, -7, 5, 64, -14]

# ----- Method 1 ----- #
print(list(filter(lambda item:item > 0,items)))

# ----- Method 2 ----- #
print([item for item in items if item >= 0])

# ----- Method 3 ----- #

i = 0
positive = []
while i < len(items):
    if items[i] >= 0:
        positive.append(items[i])
    i += 1
print(positive)