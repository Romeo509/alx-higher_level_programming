#!/usr/bin/python3
"""Defines a class MyInt."""


class MyInt(int):
    """Invert int operators is and is not."""

    def __eq__(self, value):
        """Override is opeartor with is not behavior."""
        return self.real is not value

    def __ne__(self, value):
        """Override is not operator with is behavior."""
        return self.real is value
