#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = abs(number) % 10
if number < 0:
    Last_digit = -Last_digit
print("Last digit of {} is {} and ".format(number, Last_digit), end='')
if Last_digit > 5:
    print("is greater than 5")
elif Last_digit == 0:
    print("is 0")
elif Last_digit < 6 and Last_digit != 0:
    print("is less than 6 and not 0")
