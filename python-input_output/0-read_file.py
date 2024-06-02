#!/usr/bin/python3
"""module read_file
"""


def read_file(filename=""):
    """read a file

    Args:
        filename (str, optional): file to read. Defaults to "".
    """
    with open(filename, "r") as file:
        print(file.read(), end="")
