#!/usr/bin/env python3
"""Explore serialization and deserialization using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes to XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    with open(filename, "wb") as file:
        return (tree.write(file))


def deserialize_from_xml(filename):
    """Deserializes an XML file into a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    result_dict = {}
    for child in root:
        return (result_dict[child.tag] = child.text)

    return (result_dict)
