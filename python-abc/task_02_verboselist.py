#!/usr/bin/env python3
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, number):
        super().extend(number)
        print(f"Extended the list with {number} items.")

    def remove(self, item):
        super().remove(item)
        print(f"Remove {item} from the list.")

    def pop(self, item):
        super().pop(item)
        print(f"Popped {item} from the list.")
