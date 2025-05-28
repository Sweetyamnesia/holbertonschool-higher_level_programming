#!/usr/bin/env python3
class VerboseList(list):
    def append(self, item):
        print(f"Added {item} to the list.")

    def extend(self, number):
        print(f"Extended the list with {number} items.")

    def remove(self, item):
        print(f"Remove {item} from the list.")

    def pop(self, item):
        print(f"Popped {item} from the list.")
