def swap_positions(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list

list = [1,2,3,4]
print(swap_positions(list,2,3))