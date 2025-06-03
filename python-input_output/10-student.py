#!/usr/bin/python3
"""
This module contains a class Student defined by instances attributes.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        "Initialize instance of the class Student"
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        "function that retrieves a dictionary representation of Student"
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list):
            return {key: value for key,
                    value in self.__dict__.items() if key in attrs}
        return self.__dict__
