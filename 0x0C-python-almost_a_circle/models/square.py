#!/usr/bin/python3
from models.rectangle import Rectangle
""" square """


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
