#!/usr/bin/env python3

# A subclass of Python's built-in list that adds verbose output for certain operations
class VerboseList(list):
    def append(self, item):
        # Adds a single item to the list and prints a confirmation
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        # Extends the list with multiple items and prints a confirmation
        super().extend(item)
        print(f"Extended the list with [{item}] items.")

    def remove(self, item):
        # Removes the first occurrence of the item from the list and prints a confirmation
        super().remove(item)
        print(f"Remove [{item}] from the list.")

    def pop(self, index=-1):
        # Removes and returns the item at the given position, and prints a confirmation
        item =super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
