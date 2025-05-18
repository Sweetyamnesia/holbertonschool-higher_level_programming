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

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ['.', '?', ':']:
            result += '\n'
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    return result
