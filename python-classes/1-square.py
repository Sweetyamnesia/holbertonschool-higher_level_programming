#!/usr/bin/python3
"""
This module defines a class named Square.
It is a basic example to illustrate object-oriented programming in Python.
"""


class Square:
    """
    A class that represents a square.

    This class does define one private instance attribute : size.
    """
    def __init__(self, size):
        self.size = size


# Create an instance of the Square class
s = Square(size=None)
print(s)
