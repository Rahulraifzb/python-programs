# ----- Method 1 ----- #
print([item for item in range(-8,8) if item >= 0])

# ----- Method 2 ----- #
print(list(filter(lambda item:item>=0,range(-8,8))))

# ----- Method 3 ----- #
positive_numbers = []
for item in range(-8,8):
    if item>=0:
        positive_numbers.append(item)
print(positive_numbers)

# ----- Method 4 ----- #
i = 0
positive_numbers = []
items = list(range(-8,8))
while i < len(items):
    if items[i] >= 0:
        positive_numbers.append(items[i])
    i += 1

print(positive_numbers)