#!/usr/bin/python3
"""Module 5-save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """ saves to a json file
    Args:
        my_obj: object to be saved in json file
        filename: json file with object
    """
    with open(filename, "w") as myFile:
        json.dump(my_obj, myFile)
