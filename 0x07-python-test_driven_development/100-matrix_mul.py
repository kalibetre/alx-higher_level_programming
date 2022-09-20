#!/usr/bin/python3
"""Module 100-matrix_mul

This Module contains an definition for matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """multiplies to matrices

    Args:
        m_a (list(list(int, float))): first matrix
        m_b (list(list(int, float))): second matrix

    Returns:
        list(list(int, float)): multiplication of the two matrices
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for value in row:
            if type(value) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for value in row:
            if type(value) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    m_ab = []
    for row in m_a:
        mul_row = []
        for i in range(len(m_b[0])):
            col = [row[i] for row in m_b]

            if len(row) != len(col):
                raise ValueError("m_a and m_b can't be multiplied")

            mul_row.append(sum([r * c for r, c in zip(row, col)]))
        m_ab.append(mul_row)

    return m_ab
