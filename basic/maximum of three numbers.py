# Method 1
    # def maximum(a,b,c):
    #     if a >= b and a >= c:
    #         return a
    #     elif b >= c and b >= a:
    #         return b
    #     else:
    #         return c
        

    # num1 = int(input("Enter first number: "))
    # num2 = int(input("Enter second number: "))
    # num3 = int(input("Enter third number: "))

    # print(maximum(num1,num2,num3))

# Method 2
    # def maximum(a,b,c):
    #     list = [a,b,c]

    #     return max(list)

    # num1 = int(input("Enter first number: "))
    # num2 = int(input("Enter second number: "))
    # num3 = int(input("Enter third number: "))
    # print(maximum(num1,num2,num3))

# Method 3

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print(max(num1,num2,num3))
