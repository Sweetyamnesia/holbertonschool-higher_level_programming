#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file to a JSON file.

    Args:
        filename (str): The path to the CSV file to convert.

    Returns:
        bool: True if conversion succeeds, False otherwise.
    """
    
    try:
        with open(filename, "r", encoding="utf-8") as csv_file:
            data = list(csv.DictReader(csv_file))

        """
        JSON output file is fixed as 'data.json'
        """
        json_filename = "data.json"
        with open(json_filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        return True

    except Exception:
        print("file not found")
        return False
