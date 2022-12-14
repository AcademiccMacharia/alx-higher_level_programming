#!/usr/bin/python3
"""Create a class called Square."""


class Square:
    """A class that defines a square by its size
    """
    def __init__(self, size=0):
        """Initializes the Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def area(self):
        """returns the square area.
        """
        return (self.__size * self.__size)
