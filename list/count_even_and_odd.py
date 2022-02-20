items = [10, 21, 4, 45, 66, 93, 1]
  

# ----- Method 1 ----- #
even_count, odd_count = 0, 0

for i in range(len(items)):
    if items[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count,odd_count)

# ----- Method 2 ----- #
i = 0
even_count,odd_count = 0,0
while i<len(items):
    if items[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    i += 1

print(even_count,odd_count)

# ----- Method 3 ----- #

even_count = len(list(filter(lambda item: item % 2 == 0,items)))
odd_count = len(list(filter(lambda item: item % 2 != 0,items)))
print(even_count,odd_count)
