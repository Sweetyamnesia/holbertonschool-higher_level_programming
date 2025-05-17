#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of these characters: . ? and :

Raises:
    TypeError: if text is not a string
"""


def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?' and ':'

    Args:
        text (str): the input text

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")

        if text[i] in ['.', '?', ':']:
            print()
            print()

            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
