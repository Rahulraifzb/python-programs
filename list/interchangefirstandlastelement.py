
######## --- Method 1 --- ########

# def inter_change_position(newList):
#     newList[0],newList[-1] = newList[-1],newList[0]
#     return newList

# print(inter_change_position([1,2,3,4,5,6]))

######## --- Method 2 --- ########

# def inter_change_position(newList):
#     first,*middle,last = newList
#     return [last,*middle,first]

# print(inter_change_position([1,2,3,4,5,6]))

######## --- Method 3 --- ########

def inter_change_position(newList):
    first = newList.pop(0)
    last = newList.pop(-1)
    newList.insert(0,last)
    newList.append(first)
    return newList

print(inter_change_position([1,2,3,4,5,6]))