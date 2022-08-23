#!/usr/bin/python3
for i in range(100):
    print("{i:02d}".format(i=i), end=", " if i != 99 else "\n")
