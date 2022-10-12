#!/usr/bin/python3
"""Creates a class called Square."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """Initializes the object."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the area of the square."""

        return (self.__size * self.__size)

    @property
    def size(self):
        """Method to return the size value."""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the object value."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >=0")
        else:
            self.__size = value
