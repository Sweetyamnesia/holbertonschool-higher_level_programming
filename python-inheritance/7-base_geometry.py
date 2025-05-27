#!/usr/bin/python3
"""
This module defines a class named BaseGeometry.
It is a basic example to illustrate object-oriented programming in Python.
"""


class BaseGeometry:
    """
    Represents an empty Base Geometry.

    This is a placeholder class used to illustrate the structure
    of a class in Python.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
