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
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __repr__(self):
        """
        Return a string representation of the rectangle and
        recreate a new instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"
