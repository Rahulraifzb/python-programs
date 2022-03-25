def isMonotonic(items):
    return all([items[i] <= items[i+1] for i in range(len(items) - 1)]) or all([items[i] >= items[i+1] for i in range(len(items) - 1)])


items = [5,3,7,1]
print(isMonotonic(items))