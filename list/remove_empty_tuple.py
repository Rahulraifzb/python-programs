# ----- Method 1 ----- #
# def Remove(items):
#     return [item for item in items if item ]

# print(Remove([(), ('ram','15','8'), (), ('laxman', 'sita'), 
#                   ('krishna', 'akbar', '45'), ('',''),()]
# ))

# ----- Method 2 ----- #
# def Remove(items):
#     return list(filter(None,items))

# print(Remove([(), ('ram','15','8'), (), ('laxman', 'sita'), 
#                   ('krishna', 'akbar', '45'), ('',''),()]
# ))