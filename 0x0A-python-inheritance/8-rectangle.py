#!/usr/bin/python3
"""
Definition fo class Reactangle inheriting BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(Basegeometry):
    """Defnifition of class Rectangle that inherits from BaseGeometry.
       Attributes:
            width (int): rectangle with.
            height (int) rectangle height.
    """

    def __init__(self, width, height):
        """Instance of class Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
