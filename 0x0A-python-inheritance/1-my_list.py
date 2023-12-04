#!/usr/bin/python3
"""
Defines the MyList class.
"""


class MyList(list):
    """
    A class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        sortedlist = sorted(self)
        print(sorted(self))
