items = ["Gfg","is","best","for","Geeks"]
print("Original list")

res = [item.replace("G","-").replace("e","G").replace("-","e") for item in items]

print(res)