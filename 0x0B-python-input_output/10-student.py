#!/usr/bin/python3
"""Function for class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__

        valid_attrs = filter(lambda attr: hasattr(self, attr), attrs)
        return {attr: getattr(self, attr) for attr in valid_attrs}
