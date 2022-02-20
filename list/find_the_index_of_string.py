items = ["sravan", 98, "harsha", "jyothika", "deepika", 78, 90, "ramya"]

print([pos for pos,item in enumerate(items) if type(item) == str])
print([items.index(item) for item in items if type(item) == str])
