#!/usr/bin/python3
"""function for  a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """containing a given string in a file.
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as a:
        a.write(text)
