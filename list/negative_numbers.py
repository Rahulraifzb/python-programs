items = [12, -7, 5, 64, -14]

# ----- Method 1 ----- #
print([item for item in items if item < 0])

# ----- Method 2 ----- #
print(list(filter(lambda item:item<0,items)))

# ----- Method 3 ----- #
negative_numbers = []
for i in range(len(items)):
    if items[i] < 0:
        negative_numbers.append(items[i])
print(negative_numbers)

# ----- Method 4 ----- #

i = 0
negative_numbers = []
while i < len(items):
    if items[i] < 0:
        negative_numbers.append(items[i])
    i += 1

print(negative_numbers)