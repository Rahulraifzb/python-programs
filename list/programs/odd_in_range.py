# ----- Method 1 ----- #
odds = []
start,end = 4,19
for i in range(start,end+1):
    if i % 2 != 0:
        odds.append(i)

print("Odd Numbers: ",odds)

# ----- Method 2 ----- #
odds = list(filter(lambda item:item % 2 != 0,range(start,end+1)))

print("Odd Numbers: ",odds)

# ----- Method 3 ----- #

print(list(range(3,end+1)[::2]))