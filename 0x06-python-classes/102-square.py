#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (float or int): The size of the new square.

        Raises:
            TypeError: If `size` is not a number.
            ValueError: If `size` is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If `value` is not a number.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal."""
        return not self == other

    def __lt__(self, other):
        """Check if one square is smaller than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square is smaller or equal to the other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square is greater than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square is greater or equal to the other."""
        return self.area() >= other.area()
