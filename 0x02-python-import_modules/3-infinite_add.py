#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv) - 1
    sum = 0

    for i, arg in enumerate(argv):
        if i == 0:
            continue
        sum += int(arg)

    print("{n:d}".format(n=sum))
