#!/usr/bin/python3
import json
"""module json string
"""


def to_json_string(my_obj):
    """obj to json function

    Args:
        my_obj (any, less set): object to json representation

    Returns:
        str: str json representation
    """
    return json.dumps(my_obj)
