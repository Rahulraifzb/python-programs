# Method 1

    # num1 = int(input("Enter a number: "))
    # total = 1
    # while num1 > 0:
    #     total = total * num1
    #     num1 -= 1

    # print(total)

# Method 2

    # num = int(input("Enter a number: "))
    # total = 1
    # for i in range(1,num + 1):
    #     total *= i

    # print(f"--- factorial of {num} is {total} ----")

# Method 3

    # def fact(num):
    #     if num < 0:
    #         return 0
    #     elif num == 1 or num == 0:
    #         return 1
    #     else:
    #         fact = 1
    #         while num > 0:
    #             fact *= num
    #             num -= 1

    #         return fact


    # num = int(input("Enter a number to find the factorial: "))
    # print(f"Factorial of {num} is {fact(num)}")


# Method 4 - (using recursion) 

    # def fact(num):
    #     return 1 if num == 1 or num == 0 else num * fact(num - 1)

    # num = int(input("Enter a number to find the factorial: "))
    # print(fact(num))

# Method 5 - (using built in method)

    # import math

    # def fact(num):
    #     return math.factorial(num)

    # num = int(input("Enter a number to find the factorial: "))
    # print(f"Factorial of {num} is {fact(num)}")



