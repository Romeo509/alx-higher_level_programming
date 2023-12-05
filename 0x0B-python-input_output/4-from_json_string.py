#!/usr/bin/python3
"""
Function for from_json_string.
"""


import json


def from_json_string(my_str):
    """
    Returns: an object represention of a JSON string.
    """
    return (json.loads(my_str))
