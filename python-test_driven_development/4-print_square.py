#!/usr/bin/python3
"""
Function that prints a square with character #

Size is the lenght of the square.

TypeError: Size must be an integer.

TypeError: Size must be >= 0

TypeError: size must be an integer

"""


def print_square(size):
    """
    Function that prints a square

    Args:
    size: the size length of the square.

    Returns:
    The square with #
    """

    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif not isinstance(size, (float)) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
