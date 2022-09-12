#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        value = my_list[i]
        try:
            if int(value) == value:
                print("{:d}".format(int(value)), end='')
                count += 1
        except Exception:
            pass
    print("")
    return count
