str_lists = ['Gfg', 'is', 'best', 'for', 'Geeks']


print("The original list is : ",str_lists)
res = [item.replace("G","-").replace("e","G").replace("-","e") for item in str_lists ]

print("List after performing character swaps : ",res)