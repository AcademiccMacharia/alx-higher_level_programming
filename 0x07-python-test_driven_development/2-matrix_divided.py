#!/usr/bin/python3

"""
Function that divides al elements of a matrix
"""

def matrix_divided(matrix, div):
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(div must be a number)
    if (div == 0):
        raise ZeroDivisionError(division by zero)
