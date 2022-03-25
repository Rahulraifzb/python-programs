# Method 1
# def swap_list(l):
#     size = len(l)

#     temp = l[0]
#     l[0] = l[size - 1]
#     l[size - 1] = temp

#     return l

# l = [1,2,3,4,5,6]
# print(swap_list(l))


# Method 2
# def swap_list(l):
#     l[0],l[-1] = l[-1],l[0]
#     return l

# l = [1,2,3,4,5]
# print(swap_list(l))

# Method 3
def swap_list(list):
    start,*rest,end = list
    list = [end,*rest,start]
    return list


l = [1,2,3,4,5,6]
print(swap_list(l))