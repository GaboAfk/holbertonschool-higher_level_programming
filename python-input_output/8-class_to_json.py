#!/usr/bin/python3
"""class to json module
"""


def class_to_json(obj):
    """convert obj (class) to a dictionary

    Args:
        obj (cls): simple data structure

    Returns:
        dict: class structure
    """
    return obj.__dict__
