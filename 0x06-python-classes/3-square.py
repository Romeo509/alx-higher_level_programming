#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square."""
        if not isinstance(size, int):
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size should be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of this square."""
        return (self.__size * self.__size)
