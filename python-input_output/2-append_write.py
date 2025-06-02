#!/usr/bin/python3
"""
This module contains a function that append a string at the end of a text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Prints number of characters which added at the end of text file."""
    with open(filename, "a", encoding="utf-8") as file:
        content = file.write(text)
    return (content)
