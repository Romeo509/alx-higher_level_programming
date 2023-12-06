#!/usr/bin/python3
"""
Module for load_from_json_file method.
"""


import json


def load_from_json_file(filename):
    """loads object from JSON file.
    """
    with open(filename, "r") as file:
        my_obj = json.load(file)
        return my_obj
