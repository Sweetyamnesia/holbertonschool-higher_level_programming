#!/usr/bin/python3
"""
Function that prints a string with two parameters : first name and last name.

TypeError: First must be strings.

TypeError: Last name must be a string
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints first name and last name.

    Args:
    first_name: The first argument.
    last_name: The second argument

    Returns:
    string with first and last name
    """
    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
