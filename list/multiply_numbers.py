from functools import reduce


items = [1,2,3,4,5]


# ----- Method 1 ----- #
# total = 1
# for item in items:
#     total *= item

# print("Multiply: ",total) 

# ----- Method 2 ----- #
total = reduce((lambda x,y:x*y),items)
print("Multiply: ",total)
