#!/usr/bin/env python3

# Custom iterator that keeps track of how many items have been accessed
class CountedIterator:
    def __init__(self, some_iterable):
        # Convert the input iterable into an iterator
        self.iterator = iter(some_iterable)
        # Initialize the counter
        self.count = 0

    def __iter__(self):
        # Returns the iterator object (self)
        return self

    def __next__(self):
        # increment self.count before returning the next item
        value = next(self.iterator)
        self.counter += 1
        return value

    def get_count(self):
        # Returns the number of items that have been fetched so far
        return self.count
