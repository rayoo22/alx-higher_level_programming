#!/usr/ib/python3
"""Module 6-load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an Object from a 'JSON file'
    Args:
        filename: file to create an object from
    """
    with open(filename, "r") as myFile:
        python_object = json.load(myFile)
