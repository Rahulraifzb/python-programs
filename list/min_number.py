items =  [15, 6, 7, 10, 12, 20, 10, 28, 10]


# ----- Method 1 ----- #
# min = items[0]
# for i in range(len(items)):
#     if items[i] < min:
#         min = items[i]

# print("Minimum Number: ",min)

# ----- Method 2 ----- #
# print("Minimum Number: ",min(items))

# ----- Method 3 ----- #
new_items = sorted(items)
print(*new_items[0:1])