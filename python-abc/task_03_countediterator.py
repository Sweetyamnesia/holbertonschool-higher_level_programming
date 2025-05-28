#!/usr/bin/env python3
class CountedIterator:
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.iterator)
        return value

    def get_count(self):
        return self.count
