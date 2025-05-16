#!/usr/bin/python3
"""
    Adds two numbers after checking their type.

    Numbers must be integers or floats.
    If they are floats, they are first converted to integers.

    Raises:
    TypeError: If a or b is neither an int nor a float.
"""


def add_integer(a, b=98):
    """
    Function that prints sum of 2 integers.

    Args:
    a (int or float): The first operand of the addition.
    b (int or float, optional): The second operand. Defaults to 98.

    Returns:
    int: The integer sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
