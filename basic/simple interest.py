def simple_interest(p,t,r):
    return (p * t * r) / 100

rate = int(input("Enter the rate: "))
time = int(input("Enter the time: "))
principal = int(input("Enter the principal: "))

print(f"The Simple Interest of principal {principal},time {time} and rate {rate} is {simple_interest(principal,time,rate)} ")
