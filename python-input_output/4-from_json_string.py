#!/usr/bin/python3
"""module json to python

Returns:
    obj: str to obj
"""
import json


def from_json_string(my_str):
    """from json str to python data structure

    Args:
        my_str (str): json file

    Returns:
        type: structure
    """
    return json.loads(my_str)
