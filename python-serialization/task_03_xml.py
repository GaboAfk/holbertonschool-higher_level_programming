#!/usr/bin/python3
"""xml

Returns:
    file: deserialized xml file
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key in dictionary:
        element = ET.SubElement(root, key)
        element.text = str(dictionary[key])

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    xml_data = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for element in root:
        xml_data[element.tag] = element.text

    return xml_data
