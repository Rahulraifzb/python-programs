items = [1, 1, 1, 64, 23, 64, 22, 22, 22]
res = []
for index in range(len(items) - 2):
    if items[index] == items[index + 1] and items[index + 1] == items[index + 2]:
        res.append(items[index])  
print(res)