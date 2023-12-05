#!/usr/bin/python3
"""
Definition of the class Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition for class Square inheriting from class Rectangle"""

    def __init__(self, size):
        """Initialise an instance"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of square"""
        return self.__size ** 2
