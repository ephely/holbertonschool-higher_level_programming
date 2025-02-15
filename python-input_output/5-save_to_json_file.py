#!/usr/bin/python3
"""Allows to write an obj with JSON"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, "w", encoding="utf-8") as f:
        jason = json.dump(my_obj, f)
        return (jason)
