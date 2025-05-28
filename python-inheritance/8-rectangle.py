#!/usr/bin/python3
"""
This module defines a class named BaseGeometry.
It is a basic example to illustrate object-oriented programming in Python.
"""


class BaseGeometry:
    """
    Represents an empty Base Geometry.

    This is a placeholder class used to illustrate the structure
    of a class in Python. Intended to be extended by subclasses.
    """

    def area(self):
        """
        Calculates the area of the geometry.

        This method is not implemented here because the base class
        does not know the shape. It should be overridden by subclasses.

        Raises:
            Exception: Always, indicating the method must be
            implemented in a subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the parameter (used in error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
      
    @property
    def heigth(self):
        return self.__height
