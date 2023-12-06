#!/usr/bin/python3
""" Function for student class """


class Student:
    """ student """
    def __init__(self, first_name, last_name, age):
        """ student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """  retrieves a dictionary representation of a Student """
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__
        valid_attrs = filter(lambda attr: hasattr(self, attr), attrs)
        return {attr: getattr(self, attr) for attr in valid_attrs}

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for key, value in json.items():
            setattr(self, key, value)
