#!/usr/bin/python3
"""Module 101-stats

This Module contains a script that reads stdin line by line and
computes a metrics
"""


import sys


def main():
    """main script function to read input from stdin and process it"""
    line_count = 0
    er_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0

    try:
        for line in sys.stdin:
            matches = line.split()
            if len(matches) >= 2:
                if matches[-2] in er_codes:
                    er_codes[matches[-2]] += 1
                file_size += int(matches[-1])
                line_count += 1
                if line_count % 10 == 0:
                    print_metrics(file_size, er_codes)

    except KeyboardInterrupt:
        print_metrics(file_size, er_codes)
        raise

    print_metrics(file_size, er_codes)


def print_metrics(file_size, er_codes):
    """
    computes the matrices of a set of 10 inputs or whatever is left after
    signal interrupt
    """
    print(f"File size: {file_size}")
    for code in sorted(er_codes.items(), key=lambda x: x[0]):
        if code[1] > 0:
            print(f"{code[0]}: {code[1]}")


if __name__ == "__main__":
    main()
