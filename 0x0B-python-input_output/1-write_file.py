#!/usr/bin/python3
"""
Function for write_file method.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)
       and returns the number of characters written.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return (f.write(text))
