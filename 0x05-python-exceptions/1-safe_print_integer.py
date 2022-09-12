#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value) == value:
            print("{:d}".format(int(value)))
            return True
        raise TypeError
    except Exception:
        return False
