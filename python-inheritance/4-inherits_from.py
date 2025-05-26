#!/usr/bin/python3
"""Module that defines the `is_same_class` function
to verify instance of an object.
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: Any Python object.
        a_class: the specified class

    Returns:
        True : if the object is an instance of a class
        or if it's inherited from the specified class
        False: if is not an instance of the class
    """

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
