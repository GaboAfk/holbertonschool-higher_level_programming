#!/usr/bin/python3
"""module print_sorted
"""


class MyList(list):
    """class MyList that inherits from list

    Args:
        list (int): elements
    """
    def print_sorted(self):
        print(sorted(self))
