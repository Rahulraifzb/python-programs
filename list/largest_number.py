items =  [15, 6, 7, 10, 12, 20, 10, 28, 10]

# ----- Method 1 ----- #

# largest = items[0]

# for i in range(len(items)):
#     if items[i] > largest:
#         largest = items[i]

# print("Largest number: ",largest) 

# ----- Method 2 ----- #
# print(max(items))

# ----- Method 3 ----- #
new_items = sorted(items,reverse=True)
print("Largest Number: ",*new_items[:1])