#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Create the root element
    """
    root = ET.Element('data')

    element = element(filename)
    for key, value in dictionary.items():
        "Create an element"
        child = element(key)
        child.text = str(value)
        element.append(child)
    return element


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    for child in root:
        print(child.tag, child.attrib)
