#!/usr/bin/python3

"""
Function that prints a square
"""


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (size < 0) and type(size) is float:
        raise TypeError("size must be an integer")

    for i in range(size):
        row = ''
        for j in range(size):
            row += '#'
        print(row)
