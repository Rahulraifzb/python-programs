# ----- Method 1 ----- #
# items =  ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
# key_lists = ["name","id"]

# list_of_dict = []
# for i in range(0,len(items),2):
#     list_of_dict.append({key_lists[0]:items[i],key_lists[1]:items[i+1]})

# print(list_of_dict)

# ----- Method 2 ----- #
items = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
dict_of_tuple = {}

for item in items:
    dict_of_tuple[tuple(item[:2])] = tuple(item[2:])

print(dict_of_tuple)