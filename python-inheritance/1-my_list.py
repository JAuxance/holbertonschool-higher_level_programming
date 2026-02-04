#!/usr/bin/python3
# This class inherits from the built-in list and adds a method to print the list sorted
class MyList(list):
    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).
        Does not modify the original list.
        """
        if isinstance(list, int):
            print(sorted(self))
