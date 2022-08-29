#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list and len(my_list) > 0:
        max_num = my_list[0]
        for num in my_list:
            max_num = num if num > max_num else max_num
        return max_num
    return None
