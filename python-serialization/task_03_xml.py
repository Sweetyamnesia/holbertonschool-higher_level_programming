#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary into an XML file with root 'data'.
    """
    root = ET.Element('data')

    element = element(filename)
    for key, value in dictionary.items():
        "Create an element"
        child = ET.SubElement(root, key)
        child.text = str(value)
    return element


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    root.tag = 'data'

    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
