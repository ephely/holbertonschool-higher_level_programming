#!/usr/bin/python3
"""Allows to get a py structure as a JSON str"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)
