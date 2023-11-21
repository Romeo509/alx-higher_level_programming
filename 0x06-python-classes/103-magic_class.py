#!/usr/bin/python3

"""Define a MagicClass."""

import math


class MagicClass:
    def __init__(self, radius=0):
        """Initialize a MagicClass"""
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
    """Return the area """
        return self.__radius ** 2 * math.pi

    def circumference(self):
    """Return The circumference """
        return 2 * math.pi * self.__radius
