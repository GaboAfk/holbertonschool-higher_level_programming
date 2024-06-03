#!/usr/bin/python3
"""module save json file

Returns:
    str: str file
"""
import json


def save_to_json_file(my_obj, filename):
    """save json file

    Args:
        my_obj (any): object to save
        filename (str): filename

    Returns:
        str: str file
    """
    with open(filename, "w") as file:
        return json.dump(my_obj, file)
