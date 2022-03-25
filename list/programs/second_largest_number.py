items =  [15, 6, 7, 10, 12, 20, 10, 28, 10]

# ----- Method 1 ----- #
# largest = max(items[0],items[1])
# second_largest = max(items[0],items[1])

# for i in range(len(items)):
#     if items[i] > second_largest:
#         second_largest = largest
#         largest = items[i]

#     if items[i] > second_largest and items[i] < largest:
#         second_largest = items[i]

# print(second_largest)

new_items = sorted(items,reverse=True)

print("Second largest Number: ",*new_items[1:2])