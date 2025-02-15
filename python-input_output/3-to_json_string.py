#!/usr/bin/python3
"""Allows to get an obj as a JSON representation"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""
    return json.dumps(my_obj)
