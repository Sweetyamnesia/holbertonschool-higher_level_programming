#!/usr/bin/python3
"""Module that defines the `is_same_class` function
to verify instance of an object.
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: Any Python object.
        a_class: the specified class

    Returns:
        True : if the object is exactly an instance of the specified class
        False: if is not an instance of the specified class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
