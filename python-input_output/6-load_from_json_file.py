#!/usr/bin/python3
"""module load from json file

Returns:
    any: any structure
"""
import json


def load_from_json_file(filename):
    """load json file

    Args:
        filename (str): filename

    Returns:
        type: file
    """
    with open(filename, "r") as file:
        return json.load(file)
