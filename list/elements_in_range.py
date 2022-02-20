items = [4, 5, 6, 7, 3, 9]

i,j=3,10


# ----- Method 1 ----- #
# res = True
# for item in items:
#     if item < i or item >= j:
#         res = False
#         break
# print ("Does list contain all elements in range : ",res)

# ----- Method 2 ----- #
res = all([item >= i or item < j for item in items])
print("Does list contain all elements in range : ",res)