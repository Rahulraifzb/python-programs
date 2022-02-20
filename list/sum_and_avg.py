items =  [4, 5, 1, 2, 9, 7, 10, 8.4]

# ----- Method 1 ----- #
# def sum_and_avg(items):
#     if all((type(item) == int or type(item) == float) for item in items):
#         total = 0
#         for item in items:
#             total += item
#         avg = total / len(items)
#         return total,round(avg,2)
#     return "Arguments not allowed!"

# print(sum_and_avg(items))

# ----- Method 2 ----- #
def sum_and_avg(items):
    if (all((type(item) == int or type(item) == float) for item in items)):
        total = sum(items)
        return total,round(total/len(items),3)
    return "Arguments not allowed"

print(sum_and_avg(items))