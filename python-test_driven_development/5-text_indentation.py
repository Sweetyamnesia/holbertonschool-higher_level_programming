#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of theses characters . ? and :

TypeError : text must be a string

"""


def text_indentation(text):
    if not isinstance(text, (str)):
        raise TypeError("text must be a string")
    print(f"{text}")
