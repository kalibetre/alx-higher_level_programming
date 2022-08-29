#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for line in matrix:
            print(" ".join("{:d}".format(i) for i in line))
