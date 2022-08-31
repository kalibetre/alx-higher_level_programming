#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    return sum([v1 * v2 for v1, v2 in my_list]) / sum([v for _, v in my_list])
