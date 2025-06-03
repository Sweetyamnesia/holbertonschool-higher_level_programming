#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as csv_file:
            data = list(csv.DictReader(csv_file))

        json_filename = filename.replace(".csv", ".json")
        with open(json_filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
            return True
    except Exception:
        return False
