#!/usr/bin/python3
"""
Function for class_to_json.
"""


def class_to_json(obj):
    """
        Returns: Dictionary representation with simple data structure.
    """
    return obj.__dict__
