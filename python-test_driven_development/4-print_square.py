#!/usr/bin/python3
"""print_square module
"""


def print_square(size):
    """print a square of #

    Args:
        size (int): size of the square

    Raises:
        TypeError: size is float and negative
        TypeError: size is not a integer
        ValueError: size is negative
    """
    if not size:
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#"*size)
