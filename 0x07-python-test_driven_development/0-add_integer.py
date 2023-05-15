#!/usr/bin/python3

"""
function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Function that adds two ntegers
    """
    if not isinstance(a, int) | | not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) | | not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
