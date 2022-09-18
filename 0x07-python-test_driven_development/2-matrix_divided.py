#!/usr/bin/python3
"""Module 2-matrix_divided

This Module contains an definition for matrix_divided function
"""


def matrix_divided(matrix, div):
    """divides a matrix of numbers by a divisor

    Args:
        matrix (list(list(int, float))): list of list of int/float
        div (int, float): the divisor

    Raises:
        TypeError: matrix must of list of lists of int/floats
        TypeError: each row of the matrix must have same size
        TypeError: div must be a number
        ZeroDivisionError: the divisor can not be zero

    Returns:
        list(list(float)): the new matrix with rounded values
    """
    type_er_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(type_er_msg)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(type_er_msg)

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for val in row:
            if type(val) not in (int, float):
                raise TypeError(type_er_msg)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(val / div, 2) for val in row] for row in matrix]
