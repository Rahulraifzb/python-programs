# ----- Method 1 ----- #
# def swap_position(list,pos1,pos2):
#     list[pos1],list[pos2] = list[pos2],list[pos1]
#     return list

# List = [23, 65, 19, 90]
# pos1, pos2  = 1, 3
# print(swap_position(List, pos1-1, pos2-1))

# ----- Method 2 ----- #

# def swap_position(list,pos1,pos2):
#     first = list.pop(pos1)
#     last = list.pop(pos2)

#     list.insert(pos2,first)
#     list.insert(pos1,last)

#     return list

# List = [23, 65, 19, 90]
# pos1, pos2  = 1, 3
# print(swap_position(List, pos1-1, pos2-1))



# ----------- Method 3 ---------- #
# def swap_position(list,pos1,pos2):
#     gst = list[pos2],list[pos1]
#     list[pos1],list[pos2] = gst
#     return list

# List = [23, 65, 19, 90]
# pos1, pos2  = 1, 3
# print(swap_position(List, pos1-1, pos2-1))
