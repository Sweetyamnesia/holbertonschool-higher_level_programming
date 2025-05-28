#!/usr/bin/python3
"""
Module that defines the Square class,
inheriting from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a Square that using size.

    This class inherits from Rectangle and validates its dimensions
    using the integer_validator method from the base class.
    """

    def __init__(self, size):
        """
        Initialize a new Rectangle instance with validated dimensions.

        Args:
            size (int): The size of the square.
        """

        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the square.
        Format: [Square] <size>/<size>
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: the area of the square
        """
        return self.__size ** 2
