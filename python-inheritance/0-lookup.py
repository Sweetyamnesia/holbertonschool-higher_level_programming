#!/usr/bin/python3
"""Module that defines the `lookup` function to list attributes and methods of an object."""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        list: A list of strings representing the object's attributes and methods.
    """
    return dir(obj)
