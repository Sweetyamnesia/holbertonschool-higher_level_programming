#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of theses characters . ? and :

TypeError : text must be a string

"""


def text_indentation(text):
    """
    Function that prints a text

    Args:
    text: the string to print

    Returns:
    The text.
    """

    if not isinstance(text, (str)):
        raise TypeError("text must be a string")

    for char in text:
        if char in [".", "?", ":"]:
            print(f"{char}", end="\n\n")
        else:
            print(char, end="")
