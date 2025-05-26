#!/usr/bin/python3
"""Module that defines the MyList class. 

This class inherits fromt the built-in list lcass and adds a method
to print the list in sorted (ascending) order.
"""


class MyList(list):
    """
    A subclass of list that adds a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """

        sorted_list = sorted(self)
        print(sorted_list)
