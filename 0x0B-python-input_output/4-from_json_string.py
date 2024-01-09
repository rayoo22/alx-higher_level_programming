#!/usr/bin/python3
"""Module 4-from_json_string"""
import json


def from_json_string(my_str):
    """object from its equivalent json string
    Args:
        my_str: json string representing original object
    Returns:
        object (Python data structure)
        represented by a JSON string
    """
    return json.loads(my_str)
