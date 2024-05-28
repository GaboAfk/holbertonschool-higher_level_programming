#!/usr/bin/python3
"""module lookup
"""


def lookup(obj):
    """return a returns the list of available attributes
       and methods of an object

    Args:
        obj (cls): class

    Returns:
        list: atributes and methods
    """
    return dir(obj)
