#!/usr/bin/python3
"""
This module contains a class Student defined by instances attributes.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        "function that retrieves a dictionary representation of Student"
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
