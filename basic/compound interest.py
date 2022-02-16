def compound_interest(principal,time,rate):
    amount = principal * pow((1 + rate/100),time)
    return amount - principal

print("Compound interest is", compound_interest(12000, 10.25, 5))