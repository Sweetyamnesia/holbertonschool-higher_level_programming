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

    i = 0
    while i < len(text):


        if text[i] in ['.', '?', ':']:
            print(text[i], end="")
            print('\n')
            i += 1
        else:
            print(text[i], end="")
            i += 1
