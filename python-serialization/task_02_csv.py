#!/usr/bin/python3
"""csv to json

Returns:
    file: file json with csv data
"""
import csv
import json


def convert_csv_to_json(CSVfilename):
    """csv to json

    Args:
        CSVfilename (str): csvfilename

    Returns:
        bool: true succesfull, false if dont
    """
    try:
        with open(CSVfilename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
