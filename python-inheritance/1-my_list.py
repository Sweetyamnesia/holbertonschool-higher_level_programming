#!/usr/bin/python3
"""Module that defines the MyList class.

This class inherits from the built-in list class and adds a method
to print the list in sorted (ascending) order.
"""


class MyList(list):
    """
    A subclass of list that adds a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        without modifying the original list.
        """
        return (sorted(self))
