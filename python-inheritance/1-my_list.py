#!/usr/bin/python3
"""Module that defines a class MyList which inherits from list
and adds a method to print the list sorted.
"""


class MyList(list):

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """

        sorted_list = sorted(self)
        print(sorted_list)
