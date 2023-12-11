#!/usr/bin/python3
from models.rectangle import Rectangle
""" square """


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

