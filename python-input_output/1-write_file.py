#!/usr/bin/python3
"""module write
"""


def write_file(filename="", text=""):
    """write function

    Args:
        filename (str, optional): filename to create. Defaults to "".
        text (str, optional): text to put in. Defaults to "".

    Returns:
        int: bytes writen
    """
    with open(filename, "w") as file:
        return file.write(text)
