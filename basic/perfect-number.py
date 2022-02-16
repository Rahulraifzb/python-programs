from itertools import count


number = int(input("Enter a number to check wheather a number is perfect number or not: "))

counter = 1

divisor = 0

while counter < number:
    if number % counter == 0:
        divisor += counter
    counter += 1

print(True if number == divisor else False)


