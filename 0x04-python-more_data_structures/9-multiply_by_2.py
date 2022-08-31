#!/usr/bin/python3
from re import A


def multiply_by_2(a_dictionary):
    return {k: v * v for k, v in a_dictionary.items()}
