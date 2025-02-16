#!/usr/bin/env python3
"""Reading data from one format (CSV) and converting it into another format ."""
import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON."""
    try:
        with open(filename, "r") as f:
            new_list = csv.DictReader(f)
            data = [row for row in new_list]
        with open("data.json", "w") as g:
            json.dump(data, g, indent=4)
        return True

    except Exception:
        return False
