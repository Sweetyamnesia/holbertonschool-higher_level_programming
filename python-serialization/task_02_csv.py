#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r") as csv_file:
            data = list(csv.DictReader(csv_file))

        jsonfile = filename.replace(".csv", ".json")
        with open(jsonfile, "w") as jsonfile:
            json.dump(data, jsonfile)
            return True
    except Exception:
        return False
