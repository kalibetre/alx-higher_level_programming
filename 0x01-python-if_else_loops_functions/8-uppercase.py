#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{i:c}".format(i=ord(c) - (32 if (ord(c) >
              96 and ord(c) < 123) else 0)), end="")
    print("")
