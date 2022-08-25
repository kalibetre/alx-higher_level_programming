#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_len = len(argv) - 1
    suffix_s = "" if arg_len == 1 else "s"
    suffix_mark = "." if arg_len == 0 else ":"
    print("{} argument{}{}".format(arg_len, suffix_s, suffix_mark))

    for i, arg in enumerate(argv):
        if i == 0:
            continue
        print("{}: {}".format(i, arg))
