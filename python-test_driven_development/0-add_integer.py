#!/usr/bin/python3
"""
    Module
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    This function takes two arguments, converts them to integers
    if they are not already, and returns their sum. If either
    argument is a float, it will be cast to an integer before
    performing the addition.

    Args:
        a (int or float): The first number to be added. Must
            be an integer or a float.
        b (int or float, optional): The second number to be
            added. Must be an integer or a float. Defaults to 98.

    Returns:
        int: The sum of `a` and `b` after converting them to integers.

    Raises:
        TypeError: If `a` or `b` are not integers or floats.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100)
        198
        >>> add_integer(2.5, 2.5)
        4
        >>> add_integer(-3, 3)
        0
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
