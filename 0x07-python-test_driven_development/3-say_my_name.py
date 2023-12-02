#!/usr/bin/python3
"""Describes a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Args:
        first_name (str): The first name.
        last_name (str): The last name (default is an empty string).

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError
        ("first_name must be a string or last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
