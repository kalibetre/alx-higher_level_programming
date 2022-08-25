#!/usr/bin/python3
from sys import argv

from calculator_1 import add, div, mul, sub

if __name__ == "__main__":
    arg_len = len(argv) - 1
    if arg_len != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operators = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    op = argv[2]

    if op not in operators.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    left = int(argv[1])
    right = int(argv[3])
    fun = operators.get(op, None)
    print("{} {} {} = {}".format(left, op, right, fun(left, right)))
