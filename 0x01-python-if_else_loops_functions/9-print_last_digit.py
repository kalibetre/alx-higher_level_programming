#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{i:d}".format(i=last_digit), end="")
    return last_digit
