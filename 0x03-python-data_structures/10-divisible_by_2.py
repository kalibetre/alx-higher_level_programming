#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list] if my_list else None
