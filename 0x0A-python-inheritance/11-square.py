#!/usr/bin/python3
"""Definition for the class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of class square"""

    def __init__(self, size):
        """Initializes instance """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """function for computing Square area"""
        return self.__size ** 2

    def __str__(self):
        """Returns string representation of an instance"""
        return "[{}] {}/{}".format(type(self).__name, self.__size,
                                   self.__size)
