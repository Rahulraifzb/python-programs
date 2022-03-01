number = 1234

res = 0
while number != 0:
    reminder = number%10
    res = res * 10 + reminder
    number //= 10

print(res)


