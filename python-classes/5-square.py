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

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Print the square.

        Returns:
            The square with character #.
        """
        if self.size == 0:
            print()
        else:
            print('#' * self.size)
