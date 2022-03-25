items = [1,2,3,4,5,6]
newItems1 = items[:]
newItems2 = list(items)
newItems1.append(7)
newItems2.append(9)

print(items)

print(newItems1)
print(newItems2)