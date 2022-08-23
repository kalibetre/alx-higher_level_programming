#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == j:
            continue
        print("{i:d}{j:d}".format(i=i, j=j),
              end=", " if f"{i}{j}" != "89" else "\n")
