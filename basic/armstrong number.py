num = int(input("Enter a number to find the armstrong number: "))
temp = num
arm = 0
while temp > 0:
    var = temp % 10
    arm += var**3
    temp //= 10

print("Armstrong number") if arm == num else print("not armstrong number")


