#!/usr/bin/python3
""" Module for append_write function """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file
    Args:
        filename (str): name of the file.
        text (str): Text to append to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
