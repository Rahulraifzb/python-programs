

items =  [15, 6, 7, 10, 12, 20, 10, 28, 10,13,19]

# ----- Method 1 ----- #
# print([item for item in items if item % 2 == 0])

# ----- Method 2 ----- #
# evens = list(filter(lambda num:(num % 2 == 0),items))
# print(evens)

# ----- Method 3 ----- #
# evens = []
# for i in range(len(items)):
#     if items[i] % 2 == 0:
#         evens.append(items[i])

# print("Evens: ",evens)

# ----- Method 4 ----- #
# i = 0
# evens = []
# while i<len(items):
#     if items[i] % 2 == 0:
#         evens.append(items[i])
#     i += 1

# print("Evens: ",evens)


