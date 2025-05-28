#!/usr/bin/python3
"""
This module defines a class named BaseGeometry.
It is a basic example to illustrate object-oriented programming in Python.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Importation of the BaseGeometry module"
"""


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using width and height.

    This class inherits from BaseGeometry and validates its dimensions
    using the integer_validator method from the base class.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance with validated dimensions.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError, ValueError: If width or height are not valid integers.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
