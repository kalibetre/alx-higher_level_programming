#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{i:c}".format(i=i + 97 if i % 2 != 0 else i + 65), end="")
