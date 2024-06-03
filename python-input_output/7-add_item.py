#!/usr/bin/python3
"""module add item
"""
from sys import argv
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    list_argv = load_from_json_file(filename)
except (FileNotFoundError, json.JSONDecodeError):
    list_argv = []

list_argv.extend(argv[1:])
save_to_json_file(list_argv, filename)
