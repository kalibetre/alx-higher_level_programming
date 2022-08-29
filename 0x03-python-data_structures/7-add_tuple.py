#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[0] if len(tuple_a) > 0 else 0
    a += tuple_b[0] if len(tuple_b) > 0 else 0
    b = tuple_a[1] if len(tuple_a) > 1 else 0
    b += tuple_b[1] if len(tuple_b) > 1 else 0
    return (a, b)
