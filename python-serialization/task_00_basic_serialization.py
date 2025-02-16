#!/usr/bin/env python3
"""
Adds the functionality to serialize a Python dictionary to a JSON
file and deserialize the JSON file to recreate the Python Dictionary
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save a Python dictionary."""
    with open(filename, "w", encoding="utf-8") as f:
        return (json.dump(data, f))


def load_and_deserialize(filename):
    """Load and deserialize a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
