#!/usr/bin/python3
"""Module 3-to_json_string"""
import json


def to_json_string(my_obj):
    """using json.dumps()
    Args:
        my_obj: object to convert to json
    Returns:
        json representation of my_obj
    """
    value = {
            "my_obj": my_obj
        }
    return json.dumps(value)
