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
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a user-friendly string representation of the Rectangle.

        Format: [Rectangle] <width>/<height>
        This method overrides the default string conversion to provide
        a readable and informative display of the rectangle's dimensions.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculates the area of the rectange.

        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height
