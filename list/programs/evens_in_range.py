items =  [15, 6, 7, 10, 12, 23, 10, 28, 10,13,19]

# ----- Method 1 ----- #
print([item for item in items[4:7] if item % 2 == 0])

# ----- Method 2 ----- #
print(list(filter(lambda item: item % 2 == 0,items[4:7])))

# ----- Method 3 ----- #
evens = []
for item in items[4:7]:
    if item % 2 == 0:
        evens.append(item)
print(evens)

# ----- Method 4 ----- #
evens = []
for i in range(4,7):
    if items[i] % 2 == 0:
        evens.append(items[i])
print(evens)


# ----- Method 5 ----- #
i = 4
evens = []
while i < 7:
    if items[i] % 2 == 0:
        evens.append(items[i])
    i += 1

print(evens)

