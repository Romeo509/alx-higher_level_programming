#!/usr/bin/python3
"""Definition for  a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes.
    locks the class.
    """

    __slots__ = ["first_name"]
