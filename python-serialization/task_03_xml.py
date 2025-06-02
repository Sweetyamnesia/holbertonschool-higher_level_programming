#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
	data = ET.Element('data')
	for child in root:
		print(dictionary, filename)


def deserialize_from_xml(filename):
	tree = ET.parse("dict.xml")
	filename = tree.getroot()
