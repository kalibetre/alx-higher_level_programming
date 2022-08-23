#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = -1 * (abs(number) % 10) if number < 0 else number % 10
print(f"Last digit of {number:d} is {last_digit:d} and is", end=" ")
if last_digit == 0:
    print(f"0")
elif last_digit > 5:
    print(f"greater than 5")
else:
    print(f"less than 6 and not 0")
