#!/usr/bin/python3
"""
This module defines a class named Square.
It is a basic example to illustrate object-oriented programming in Python.
"""


class Square:
    """
    A class that represents a square.

    This class define one private instance attribute : size.
    """
    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square. Must be a non-negative integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2
