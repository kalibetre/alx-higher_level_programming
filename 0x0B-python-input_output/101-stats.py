#!/usr/bin/python3
"""Module 101-stats

This Module contains a script that reads stdin line by line and
computes a metrics
"""


import re
import sys

regex = r"((?:\d{1,3}\.{0,1}){4}) - \[(.+)\] \"(.+)\" (\d{3}) (\d+)"


def main():
    """main script function to read input from stdin and process it"""
    chunk = []
    er_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0

    try:
        for line in sys.stdin:
            chunk.append(line)
            if len(chunk) == 10:
                file_size, er_codes = print_metrics(
                    chunk, file_size, er_codes)
                chunk.clear()
    except KeyboardInterrupt:
        print_metrics(chunk, file_size, er_codes)
        raise

    print_metrics(chunk, file_size, er_codes)


def print_metrics(chunk, file_size, er_codes):
    """
    computes the matrices of a set of 10 inputs or whatever is left after
    signal interrupt
    """
    for line in chunk:
        matches = re.finditer(regex, line)
        match = next(matches, None)
        if match.group(4) in er_codes:
            er_codes[match.group(4)] += 1
        file_size += int(match.group(5))
    print(f"File size: {file_size}")
    for code in sorted(er_codes.items(), key=lambda x: x[0]):
        if int(code[1]) > 0:
            print(f"{code[0]}: {code[1]}")

    return file_size, er_codes


if __name__ == "__main__":
    main()
