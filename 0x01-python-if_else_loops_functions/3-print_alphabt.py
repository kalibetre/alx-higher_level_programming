#!/usr/bin/python3
for i in range(26):
    if i == 16 or i == 4:
        continue
    print("{i:c}".format(i=i + 97), end="")
