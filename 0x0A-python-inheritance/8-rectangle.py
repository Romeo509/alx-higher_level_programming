#!/usr/bin/python3
"""
Definition for class Reactangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(Basegeometry):
    """Defnifition of class Rectangle.
       Attributes:
            width (int): width of the rectangle.
            height (int) height of the rectangle.
    """

    def __init__(self, width, height):
        """Instance of class Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
