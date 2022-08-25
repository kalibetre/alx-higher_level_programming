#!/usr/bin/python3
print(*list(map(lambda x: format(x, "c"), [*range(65, 91)])), sep="")
