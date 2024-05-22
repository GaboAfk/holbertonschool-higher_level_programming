#!/usr/bin/python3
"""say my name module
"""


def say_my_name(first_name, last_name=""):
    """prints first_name and last_name

    Args:
        first_name (str): first string
        last_name (str, optional): second string. Defaults to "".

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
