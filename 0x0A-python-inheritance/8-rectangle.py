#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height
