#!/usr/bin/python3
"""module basic deserialization"""
import json


def serialize_and_save_to_file(data, filename):
    """serialize to json

    Args:
        data (structure): data to save
        filename (str): filename

    Returns:
        str: json str
    """
    with open(filename, "w") as file:
        return json.dump(data, file)


def load_and_deserialize(filename):
    """deserialize from json

    Args:
        filename (str): filename

    Returns:
        structure: data to load
    """
    with open(filename, "r") as file:
        return json.load(file)
