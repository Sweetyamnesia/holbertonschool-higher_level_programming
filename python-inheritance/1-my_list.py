#!/usr/bin/python3
"""Module that defines the `print_sorted` function
to write a class that inherits from a list
"""


class MyList(list):

    def print_sorted(self):
        """
        Returns the list in ascending sort.

        Args:
            self.

        Returns:
            list: A list of int
        """
        sorted_list = sorted(self)
        print(sorted_list)
