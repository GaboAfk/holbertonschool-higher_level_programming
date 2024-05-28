#!/usr/bin/python3
"""same class module
"""


def is_same_class(obj, a_class):
    """ function that returns True if the object is exactly an instance of the
        specified class ; otherwise False.

    Args:
        obj (any): _description_
        a_class (any): _description_

    Returns:
        bool: True if the object is exactly an instance of the specified class
        otherwise False.
    """
    return type(obj) is a_class
