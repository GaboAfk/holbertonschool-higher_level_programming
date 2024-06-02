#!/usr/bin/python3
"""module append
"""


def append_write(filename="", text=""):
    """append function

    Args:
        filename (str, optional): filename. Defaults to "".
        text (str, optional): text to append. Defaults to "".

    Returns:
        int: count of bytes
    """
    with open(filename, "a") as file:
        return file.write(text)
