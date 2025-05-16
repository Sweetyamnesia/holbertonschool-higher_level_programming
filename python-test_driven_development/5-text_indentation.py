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

    new_line = False
    for char in text:
        if new_line and char == " ":
            continue
        new_line = False

        print(char, end="")
        if char in [".", "?", ":"]:
            print("\n")
            new_line = True
