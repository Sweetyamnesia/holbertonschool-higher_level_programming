#!/usr/bin/python3
"""
This module contains a function that reads and prints
the contents of a text file.
"""

def read_file(filename=""):
    """Reads a text file and prints its contents."""
    with open(filename, "r") as file:
        content = file.read()
    print(content)
