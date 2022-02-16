# First Way
# def maximum(a,b):
#     if a >= b:
#         return a
#     return b

# num1 = int(input("Enter first number:  "))
# num2 = int(input("Enter second number:  "))
# print(f"{maximum(num1,num2)} is the grestest number") 


# Second Way
# num1 = int(input("Enter first number:  "))
# num2 = int(input("Enter second number:  "))

# maximum = max(num1,num2)
# print(f"{maximum} is the grestest number")

# Third Way
num1 = int(input("Enter first number:  "))
num2 = int(input("Enter second number:  "))

# Use of ternary Operator
print(f"{num1 if num1 >= num2 else num2} is the grestest number")
