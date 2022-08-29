#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    my_list_copy = my_list[:]
    if idx >= 0 and idx < len(my_list):
        my_list_copy[idx] = element
    return my_list_copy
