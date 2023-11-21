#!/usr/bin/python3

"""Define the module."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square."""
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """set the current size of the square."""
        return self.__size

    def area(self):
        """Return the current area of the square. """
        return self.__size ** 2

    @size.setter
    def size(self, value):
        """set the current size of the square """
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square with the character"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
