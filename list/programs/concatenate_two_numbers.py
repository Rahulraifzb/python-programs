from math import remainder
from operator import index


N = 4 
numbers = [1, 212, 12, 12]
X = 1212

s = ""
count = 0

# ------ Method 1 ------ #

# for index1,item1 in enumerate(numbers):
#     for index2,item2 in enumerate(numbers):
#         if index1 != index2:
#             if (str(item1) + str(item2)) == str(X):
#                 count += 1

# print(count)

# ------ Method 2 ------ #

# for index1,item1 in enumerate(numbers):
#     index2 = 0
#     while index2 < N:
#         if index1 != index2:
#             if (str(item1) + str(numbers[index2])) == str(X):
#                 count += 1

#         index2 += 1


# ------ Method 3 ------ #
# index1 = 0
# while (index1 < N):
#     index2 = 0
#     while index2 < N:
#         if index1 != index2:
#             if (str(numbers[index1]) + str(numbers[index2])) == str(X):
#                 count += 1
#         index2 += 1
#     index1 += 1  





# Method 4
count = {}
for i in numbers:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1

divisor = 10
divident = X
ans = 0
while divident > 0:
    divident = X//divisor
    reminder = X%divisor
    divisor *= 10
   

    if (divident in count) and (reminder in count) and ( (str(divident) + str(reminder) ) == str(X)):
        if(reminder == divident):
            ans += count[reminder]* (count[reminder] -1)
        else:
            ans += count[reminder] * count[divident]
        

print(ans)

